from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class RegistroEmpleadoPayload(BaseModel):
    nombre: str = Field(..., description="Nombre completo", min_length=3, max_length=80)
    email: EmailStr = Field(..., description="Correo electrónico")

class RegistroEmpleadoResponse(BaseModel):
    ok: bool
    message: str
    id: Optional[int] = None
