import os
import requests

def download_from_drive(file_id, dest_path):
    # Garante que a pasta existe antes de salvar o arquivo
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    URL = "https://drive.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)
    token = None
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            token = value
    if token:
        response = session.get(URL, params={'id': file_id, 'confirm': token}, stream=True)
    with open(dest_path, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)

def ensure_model(model_path, file_id):
    if not os.path.exists(model_path):
        print("Baixando modelo do Google Drive")
        download_from_drive(file_id, model_path)
        print("Download concluído.")

ensure_model("ml_models/pha_classifier.pkl", "1nrKe7WgEuih3OxmUrAeTwpoeJPEvNbef")

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import simulation

app = FastAPI(
    title="NASA Hackathon - Meteor Madness API",
    description="API para simulação de impacto de asteroides.",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # URL do seu frontend
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(simulation.router, prefix="/api/v1", tags=["Simulation"])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bem-vindo à API do Simulador de Impacto!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)