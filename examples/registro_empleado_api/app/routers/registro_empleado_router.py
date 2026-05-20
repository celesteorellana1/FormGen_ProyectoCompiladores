from fastapi import APIRouter, HTTPException
from app.schemas.registro_empleado_schemas import RegistroEmpleadoPayload, RegistroEmpleadoResponse
from app.services.registro_empleado_service import create_registro_empleado

router = APIRouter(tags=["forms"])

@router.post('/api/empleados', response_model=RegistroEmpleadoResponse)
async def submit_registro_empleado(payload: RegistroEmpleadoPayload):
    try:
        return create_registro_empleado(payload)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'Error interno: {ex}')
