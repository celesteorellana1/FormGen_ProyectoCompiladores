from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class RegistroCompletoPayload(BaseModel):
    nombre: str = Field(..., description="Nombre completo", min_length=3, max_length=80)
    email: EmailStr = Field(..., description="Correo electrónico")
    password: str = Field(..., description="Contraseña", min_length=8)
    fecha_nacimiento: str = Field(..., description="Fecha de nacimiento")
    puesto: str = Field(..., description="Puesto", json_schema_extra={'options': ["Desarrollador", "Diseñador", "Analista", "Gerente"]})
    salario: Optional[float] = Field(None, description="Salario mensual", ge=1000.0, le=99999.99)
    edad: Optional[int] = Field(None, description="Edad", ge=18.0, le=65.0)
    descripcion: Optional[str] = Field(None, description="Descripción del perfil", max_length=500)
    activo: bool = Field("true", description="Cuenta activa")
    readonly_field: str = Field("EMP-000", description="Código de empleado")

class RegistroCompletoResponse(BaseModel):
    ok: bool
    message: str
    id: Optional[int] = None
