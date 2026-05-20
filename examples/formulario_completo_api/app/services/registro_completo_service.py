from app.schemas.registro_completo_schemas import RegistroCompletoPayload, RegistroCompletoResponse

_FAKE_DB = []

def create_registro_completo(payload: RegistroCompletoPayload) -> RegistroCompletoResponse:
    record = payload.model_dump()
    new_id = len(_FAKE_DB) + 1
    record['id'] = new_id
    _FAKE_DB.append(record)
    return RegistroCompletoResponse(ok=True, message='Registro procesado correctamente', id=new_id)
