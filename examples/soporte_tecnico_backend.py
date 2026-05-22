from typing import Any
from typing import Literal
from datetime import date
from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title='SoporteTecnico')

class SoporteTecnicoPayload(BaseModel):
    model_config = {"extra": "forbid"}

    nombre: str = Field(..., title='Nombre completo', description='Placeholder: Tu nombre', min_length=3, max_length=80)
    email: EmailStr = Field(..., title='Correo electrónico')
    telefono: str | None = Field(None, title='Teléfono (opcional)', description='Placeholder: +502 1234-5678', min_length=8, max_length=15)
    categoria: Literal['Hardware', 'Software', 'Red', 'Cuenta', 'Otro'] = Field(..., title='Categoría del problema')
    prioridad: Literal['Baja', 'Media', 'Alta', 'Crítica'] = Field(..., title='Prioridad')
    fecha_incidente: date = Field(..., title='Fecha del incidente')
    descripcion: str = Field(..., title='Descripción del problema', description='Placeholder: Describe el problema con el mayor detalle posible...', min_length=20, max_length=1000)
    numero_equipo: str | None = Field(None, title='Número de equipo / serial', description='Placeholder: Ej: PC-042 o SN123456', max_length=50)
    acepta_seguimiento: bool = Field('true', title='Acepto recibir actualizaciones por correo')

class SubmitResponse(BaseModel):
    ok: bool
    message: str
    redirect_to: str | None = None
    data: dict[str, Any] | None = None

@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/api/soporte/tickets", response_model=SubmitResponse, tags=["SoporteTecnico"])
async def soportetecnico(payload: SoporteTecnicoPayload = Body(...)) -> SubmitResponse:
    try:
        data = payload.model_dump()
                                                                                      
        return SubmitResponse(ok=True, message='Tu ticket fue enviado correctamente', redirect_to='/soporte/confirmacion', data=data)
    except Exception as exc:
        raise HTTPException(status_code=400, detail='Error al enviar el ticket, intenta de nuevo' + ': ' + str(exc)) from exc

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
