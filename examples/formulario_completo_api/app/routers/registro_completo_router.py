from fastapi import APIRouter, HTTPException
from app.schemas.registro_completo_schemas import RegistroCompletoPayload, RegistroCompletoResponse
from app.services.registro_completo_service import create_registro_completo

router = APIRouter(tags=["forms"])

@router.post('/api/registro', response_model=RegistroCompletoResponse)
async def submit_registro_completo(payload: RegistroCompletoPayload):
    try:
        return create_registro_completo(payload)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'Error interno: {ex}')
