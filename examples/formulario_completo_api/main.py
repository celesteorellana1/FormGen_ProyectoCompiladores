# Generado automaticamente por FormGem - API para RegistroCompleto
from fastapi import FastAPI
from app.routers.registro_completo_router import router as registro_completo_router

app = FastAPI(title="RegistroCompleto API")
app.include_router(registro_completo_router)

@app.get('/health')
async def health():
    return {'status': 'ok'}
