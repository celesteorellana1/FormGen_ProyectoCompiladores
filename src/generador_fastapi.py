import os
from typing import Dict, List


def _snake(text: str) -> str:
    out = []
    for i, ch in enumerate(text):
        if ch.isupper() and i > 0:
            out.append("_")
        out.append(ch.lower())
    return "".join(out)


def _py_str(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def _field_type_annotation(field):
    t = field.field_type
    if t in {"string", "email", "password", "textarea", "date", "select"}:
        return "str"
    if t == "int":
        return "int"
    if t == "float":
        return "float"
    if t == "boolean":
        return "bool"
    return "str"


def _field_validation(field) -> str:
    args = []
    if field.is_required:
        default = "..."
    elif field.default_val is not None:
        if isinstance(field.default_val, str):
            default = f"\"{_py_str(field.default_val)}\""
        elif isinstance(field.default_val, (int, float)):
            default = str(field.default_val)
        else:
            default = "True" if str(field.default_val).lower() == "true" else "False"
    else:
        default = "None"

    if field.label:
        args.append(f'description="{_py_str(field.label)}"')
    if field.min_length is not None:
        args.append(f"min_length={field.min_length}")
    if field.max_length is not None:
        args.append(f"max_length={field.max_length}")
    if field.min_val is not None:
        args.append(f"ge={field.min_val}")
    if field.max_val is not None:
        args.append(f"le={field.max_val}")
    if field.field_type == "select" and field.options:
        opts = ", ".join(f'"{_py_str(o)}"' for o in field.options)
        args.append(f"json_schema_extra={{'options': [{opts}]}}")

    if args:
        return f"Field({default}, {', '.join(args)})"
    return f"Field({default})"


def _sqlalchemy_column(field) -> str:
    nullable = "False" if field.is_required else "True"
    unique = "True" if "unique" in field.props_seen else "False"
    t = field.field_type
    if t in {"string", "email", "password", "textarea", "select"}:
        sql_t = f"String({field.max_length})" if field.max_length else "String(255)"
    elif t == "date":
        sql_t = "Date"
    elif t == "int":
        sql_t = "Integer"
    elif t == "float":
        sql_t = "Float"
    elif t == "boolean":
        sql_t = "Boolean"
    else:
        sql_t = "String(255)"
    return f"{field.name} = Column({sql_t}, nullable={nullable}, unique={unique})"


def _render_main(form_name: str, module_name: str) -> str:
    return "\n".join([
        f"# Generado automaticamente por FormGem - API para {form_name}",
        "from fastapi import FastAPI",
        f"from app.routers.{module_name}_router import router as {module_name}_router",
        "",
        f'app = FastAPI(title="{_py_str(form_name)} API")',
        f"app.include_router({module_name}_router)",
        "",
        "@app.get('/health')",
        "async def health():",
        "    return {'status': 'ok'}",
        "",
    ])


def _render_schemas(form_name: str, fields: list) -> str:
    model_name = f"{form_name}Payload"
    response_name = f"{form_name}Response"
    lines: List[str] = [
        "from pydantic import BaseModel, Field, EmailStr",
        "from typing import Optional",
        "",
        f"class {model_name}(BaseModel):",
    ]
    if not fields:
        lines.append("    pass")
    for f in fields:
        ann = "EmailStr" if f.field_type == "email" else _field_type_annotation(f)
        if not f.is_required and f.default_val is None:
            ann = f"Optional[{ann}]"
        lines.append(f"    {f.name}: {ann} = {_field_validation(f)}")
    lines.extend([
        "",
        f"class {response_name}(BaseModel):",
        "    ok: bool",
        "    message: str",
        "    id: Optional[int] = None",
        "",
    ])
    return "\n".join(lines)


def _render_service(form_name: str, payload_model: str, response_model: str) -> str:
    module = _snake(form_name)
    return "\n".join([
        f"from app.schemas.{module}_schemas import {payload_model}, {response_model}",
        "",
        "_FAKE_DB = []",
        "",
        f"def create_{module}(payload: {payload_model}) -> {response_model}:",
        "    record = payload.model_dump()",
        "    new_id = len(_FAKE_DB) + 1",
        "    record['id'] = new_id",
        "    _FAKE_DB.append(record)",
        f"    return {response_model}(ok=True, message='Registro procesado correctamente', id=new_id)",
        "",
    ])


def _render_router(form_name: str, method: str, route: str) -> str:
    module = _snake(form_name)
    payload_model = f"{form_name}Payload"
    response_model = f"{form_name}Response"
    return "\n".join([
        "from fastapi import APIRouter, HTTPException",
        f"from app.schemas.{module}_schemas import {payload_model}, {response_model}",
        f"from app.services.{module}_service import create_{module}",
        "",
        'router = APIRouter(tags=["forms"])',
        "",
        f"@router.{method.lower()}('{route}', response_model={response_model})",
        f"async def submit_{module}(payload: {payload_model}):",
        "    try:",
        f"        return create_{module}(payload)",
        "    except Exception as ex:",
        "        raise HTTPException(status_code=500, detail=f'Error interno: {ex}')",
        "",
    ])


def _render_db_model(form_name: str, fields: list) -> str:
    lines = [
        "from sqlalchemy import Column, Integer, String, Float, Boolean, Date",
        "from sqlalchemy.orm import declarative_base",
        "",
        "Base = declarative_base()",
        "",
        f"class {form_name}Model(Base):",
        f"    __tablename__ = '{_snake(form_name)}'",
        "    id = Column(Integer, primary_key=True, autoincrement=True)",
    ]
    for f in fields:
        lines.append(f"    {_sqlalchemy_column(f)}")
    lines.append("")
    return "\n".join(lines)


def generate_fastapi_project(result: dict, source_filename: str = "", include_db_model: bool = False) -> Dict[str, str]:
    if not result["ok"]:
        raise ValueError("No se puede generar FastAPI: el analisis semantico reporto errores.")
    form = result["form"]
    if form is None:
        raise ValueError("El resultado no contiene informacion de formulario.")

    fields = [f for s in form.sections for f in s.fields if not f.is_hidden]
    form_name = form.name
    module = _snake(form_name)
    endpoint_cfg = result.get("on_submit") or {}
    method = (endpoint_cfg.get("method") or "POST").upper()
    route = endpoint_cfg.get("url") or f"/api/{module}"

    files: Dict[str, str] = {
        "main.py": _render_main(form_name, module),
        os.path.join("app", "__init__.py"): "",
        os.path.join("app", "routers", "__init__.py"): "",
        os.path.join("app", "services", "__init__.py"): "",
        os.path.join("app", "schemas", "__init__.py"): "",
        os.path.join("app", "routers", f"{module}_router.py"): _render_router(form_name, method, route),
        os.path.join("app", "services", f"{module}_service.py"): _render_service(
            form_name, f"{form_name}Payload", f"{form_name}Response"
        ),
        os.path.join("app", "schemas", f"{module}_schemas.py"): _render_schemas(form_name, fields),
    }

    if include_db_model:
        files[os.path.join("app", "models", "__init__.py")] = ""
        files[os.path.join("app", "models", f"{module}_model.py")] = _render_db_model(form_name, fields)

    return files
