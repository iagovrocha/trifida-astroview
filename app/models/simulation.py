# app/models/simulation.py

from pydantic import BaseModel
from typing import Dict, Any, Optional

class SimulationRequest(BaseModel):
    diameter_km: float
    velocity_km_s: float
    impact_angle: float
    impact_lat: float
    impact_lng: float
    asteroid_type: str

class SimulationResponse(BaseModel):
    kpis: Dict[str, Any] = {
        "population_in_risk": 0,
        "impact_energy_megatons": 0.0,
        "final_damage_radius_km": 0.0,
        "is_pha_prediction": False,
        "risk_assessment_source": "N/A"
    }
    
    details: Dict[str, Any] = {
        "input_params": {},
        "scenario_params": {},
        "physics_output": {},
        "llm_report": ""
    }

class ChatRequest(BaseModel):
    question: str
    context: dict 