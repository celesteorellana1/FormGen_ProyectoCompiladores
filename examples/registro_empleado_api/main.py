# Generado automaticamente por FormGem - API para RegistroEmpleado
from fastapi import FastAPI
from app.routers.registro_empleado_router import router as registro_empleado_router

app = FastAPI(title="RegistroEmpleado API")
app.include_router(registro_empleado_router)

@app.get('/health')
async def health():
    return {'status': 'ok'}
