from app.schemas.registro_empleado_schemas import RegistroEmpleadoPayload, RegistroEmpleadoResponse

_FAKE_DB = []

def create_registro_empleado(payload: RegistroEmpleadoPayload) -> RegistroEmpleadoResponse:
    record = payload.model_dump()
    new_id = len(_FAKE_DB) + 1
    record['id'] = new_id
    _FAKE_DB.append(record)
    return RegistroEmpleadoResponse(ok=True, message='Registro procesado correctamente', id=new_id)
