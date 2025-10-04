import uvicorn
from fastapi import FastAPI
from app.api.endpoints import simulation

app = FastAPI(
    title="NASA Hackathon - Meteor Madness API",
    description="API para simulação de impacto de asteroides.",
    version="1.0.0"
)

app.include_router(simulation.router, prefix="/api/v1", tags=["Simulation"])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bem-vindo à API do Simulador de Impacto!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)