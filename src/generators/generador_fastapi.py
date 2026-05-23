import os
import re
import sys
from typing import Any

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "generated"))

# Helpers de formato de nombres

def _pascal_case(text: str) -> str:
    parts = re.split(r"[^a-zA-Z0-9]+", text)
    cleaned = [p for p in parts if p]
    if not cleaned:
        return "FormData"
    return "".join(p[0].upper() + p[1:] for p in cleaned)

def _snake_case(text: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_").lower()
    return value or "submit_form"

def _py_repr(value: Any) -> str:
    if isinstance(value, str):
        return repr(value)
    if isinstance(value, bool):
        return "True" if value else "False"
    return repr(value)

# Resolución de tipos Pydantic por campo

def _make_type_for_field(field) -> tuple[str, list[str], bool]:
    field_type = getattr(field, "field_type", "string")
    if field_type == "email":
        return "EmailStr", ["EmailStr"], True
    if field_type == "int":
        return "int", [], False
    if field_type == "float":
        return "float", [], False
    if field_type == "date":
        return "date", ["date"], False
    if field_type == "boolean":
        return "bool", [], False
    if field_type == "select":
        options = getattr(field, "options", []) or []
        if options:
            literal_opts = ", ".join(_py_repr(o) for o in options)
            return f"Literal[{literal_opts}]", ["Literal"], False
        return "str", [], True
    return "str", [], True

# Construcción del modelo Pydantic

def _build_model(form) -> tuple[list[str], list[str]]:
    imports = {"Any"}
    lines = []

    model_name = f"{_pascal_case(form.name)}Payload"
    lines.append(f"class {model_name}(BaseModel):")
    lines.append('    model_config = {"extra": "forbid"}')
    lines.append("")

    all_fields = [field for section in form.sections for field in section.fields]
    if not all_fields:
        lines.append("    pass")
        return lines, sorted(imports)

    for field in all_fields:
        field_name = field.name
        py_type, needed_imports, is_text = _make_type_for_field(field)
        imports.update(needed_imports)

        default_expr = "..."
        is_required = getattr(field, "is_required", False)
        default_val = getattr(field, "default_val", None)
        if default_val is not None:
            default_expr = _py_repr(default_val)
            is_required = False
        elif not is_required:
            py_type = f"{py_type} | None"
            default_expr = "None"

        field_args = []
        label = getattr(field, "label", None)
        placeholder = getattr(field, "placeholder", None)
        min_length = getattr(field, "min_length", None)
        max_length = getattr(field, "max_length", None)
        min_val = getattr(field, "min_val", None)
        max_val = getattr(field, "max_val", None)

        if label:
            field_args.append(f"title={_py_repr(label)}")
        if placeholder:
            field_args.append(f"description={_py_repr(f'Placeholder: {placeholder}')}")

        if is_text:
            if min_length is not None:
                field_args.append(f"min_length={min_length}")
            if max_length is not None:
                field_args.append(f"max_length={max_length}")
        else:
            if min_val is not None:
                field_args.append(f"ge={min_val}")
            if max_val is not None:
                field_args.append(f"le={max_val}")

        schema_extra = {}
        if getattr(field, "is_unique", False):
            schema_extra["unique"] = True
        if getattr(field, "is_hidden", False):
            schema_extra["hidden"] = True
        if getattr(field, "is_readonly", False):
            schema_extra["readonly"] = True
        if schema_extra:
            field_args.append(f"json_schema_extra={_py_repr(schema_extra)}")

        args_suffix = ""
        if field_args:
            args_suffix = ", " + ", ".join(field_args)

        lines.append(f"    {field_name}: {py_type} = Field({default_expr}{args_suffix})")

    return lines, sorted(imports)

# Generación del archivo Python completo

def generate(result: dict, source_filename: str = "") -> str:
    if not result.get("ok"):
        raise ValueError("No se puede generar FastAPI: el análisis semántico reportó errores.")

    form = result.get("form")
    if form is None:
        raise ValueError("El resultado no contiene información de formulario.")

    _os = result.get("on_submit")
    if _os is None:
        on_submit = {}
    elif isinstance(_os, dict):
        on_submit = _os
    else:
        on_submit = {
            "method":      getattr(_os, "method",      None),
            "url":         getattr(_os, "url",         None),
            "success_msg": getattr(_os, "success_msg", None),
            "error_msg":   getattr(_os, "error_msg",   None),
            "success_url": getattr(_os, "success_url", None),
        }

    method = (on_submit.get("method") or "POST").upper()
    if method not in {"GET", "POST"}:
        method = "POST"
    submit_url = on_submit.get("url") or "/api/submit"
    success_msg = on_submit.get("success_msg") or "Operación exitosa"
    error_msg = on_submit.get("error_msg") or "Error al procesar"
    success_url = on_submit.get("success_url")

    model_lines, import_names = _build_model(form)
    model_name = f"{_pascal_case(form.name)}Payload"
    handler_name = _snake_case(form.name)
    decorator = "get" if method == "GET" else "post"

    base = os.path.basename(source_filename) if source_filename else "formulario.fg"
    out = []
    out.append(f"# Generado automáticamente por FormGem - fuente: {base}")
    out.append("# Backend FastAPI")
    out.append("")
    out.append("from typing import Any")
    if "Literal" in import_names:
        out.append("from typing import Literal")
    if "date" in import_names:
        out.append("from datetime import date")
    out.append("from fastapi import Body, FastAPI, HTTPException")
    if "EmailStr" in import_names:
        out.append("from pydantic import BaseModel, EmailStr, Field")
    else:
        out.append("from pydantic import BaseModel, Field")
    out.append("")
    _form_title = getattr(form, "title", None) or getattr(form, "name", None) or "FormGem API"
    out.append(f'app = FastAPI(title={_py_repr(_form_title)})')
    out.append('')
    out.append('from fastapi.middleware.cors import CORSMiddleware')
    out.append('app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])')
    out.append('')
    out.append("")
    out.extend(model_lines)
    out.append("")
    out.append("class SubmitResponse(BaseModel):")
    out.append("    ok: bool")
    out.append("    message: str")
    out.append("    redirect_to: str | None = None")
    out.append("    data: dict[str, Any] | None = None")
    out.append("")
    out.append('@app.get("/health", tags=["health"])')
    out.append("async def health() -> dict[str, str]:")
    out.append('    return {"status": "ok"}')
    out.append("")
    out.append(f'@app.{decorator}("{submit_url}", response_model=SubmitResponse, tags=["{form.name}"])')
    out.append(f"async def {handler_name}(payload: {model_name} = Body(...)) -> SubmitResponse:")
    out.append("    try:")
    out.append("        data = payload.model_dump()")
    out.append("        # TODO: conectar persistencia / reglas de negocio (por ejemplo, unique en BD).")
    out.append(f"        return SubmitResponse(ok=True, message={_py_repr(success_msg)}, redirect_to={_py_repr(success_url)}, data=data)")
    out.append("    except Exception as exc:")
    out.append(f"        raise HTTPException(status_code=400, detail={_py_repr(error_msg)} + ': ' + str(exc)) from exc")
    out.append("")
    out.append('if __name__ == "__main__":')
    out.append("    import uvicorn")
    out.append('    uvicorn.run(app, host="127.0.0.1", port=8000)')
    out.append("")
    return "\n".join(out)
