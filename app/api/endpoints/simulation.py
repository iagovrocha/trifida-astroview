from fastapi import APIRouter, HTTPException
from app.models.simulation import SimulationRequest, SimulationResponse
from app.core.constants import SCENARIOS, CATASTROPHIC_THRESHOLD_MT, ASTEROID_TYPE_MAPPING
import google.generativeai as genai
from app.models.simulation import ChatRequest
from app.services.simulation_engine import calculate_damage_from_pair_model, predict_pha_risk
from app.services.geo_analysis import get_population_in_radius, get_economic_impact
from app.services.llm_services import gemini_model

router = APIRouter()


@router.post("/simulate", response_model=SimulationResponse)
async def run_synchronous_simulation(request: SimulationRequest):
    """
    Executes the complete simulation (physics, AI, geolocation) and returns 
    a structured object with KPIs and details.
    """
    print(f"--- STARTING NEW SIMULATION ---")
    print(f"User input: {request.dict()}")

    try:
        print("Step A: Running physics calculations...")
        asteroid_type = request.asteroid_type
        
        # Check if asteroid type needs mapping from English to Portuguese
        if asteroid_type in ASTEROID_TYPE_MAPPING:
            mapped_asteroid_type = ASTEROID_TYPE_MAPPING[asteroid_type]
            print(f"Mapping asteroid type: {asteroid_type} -> {mapped_asteroid_type}")
        else:
            mapped_asteroid_type = asteroid_type
        
        # Validate the mapped asteroid type
        if mapped_asteroid_type not in SCENARIOS:
            valid_types = list(ASTEROID_TYPE_MAPPING.keys()) + list(SCENARIOS.keys())
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid asteroid type: {asteroid_type}. Valid types: {valid_types}"
            )
        
        scenario_params = SCENARIOS.get(mapped_asteroid_type)
        engine_args = {
            "diameter_km": request.diameter_km,
            "velocity_km_s": request.velocity_km_s,
            "impact_angle": request.impact_angle,
            "densidade_rho": scenario_params["densidade_rho"],
            "eficiencia_eta": scenario_params["eficiencia_eta"]
        }
        physics_results = calculate_damage_from_pair_model(**engine_args)
        print(" -> Physics OK!")

        print("Step B: Running AI prediction...")
        ml_features = {
            'absolute_magnitude_h': 22.0, 'diameter_km_avg': request.diameter_km,
            'velocity_km_s': request.velocity_km_s, 'miss_distance_km': 10000000,
            'kinetic_energy_joules': physics_results['kinetic_energy_joules']
        }
        pha_prediction = predict_pha_risk(ml_features)
        print(" -> AI OK!")

        print("Step D: Applying safety rule...")
        final_pha_risk = pha_prediction
        risk_source = "Machine Learning"

        if physics_results['energia_megatons'] > CATASTROPHIC_THRESHOLD_MT:
            final_pha_risk = True
            risk_source = "Physics Safety Rule"
        print(" -> Risk Analysis OK!")

        print("Step C: Calculating geographic impact...")
        final_radius_km = physics_results['raio_dano_final_km']
        population_in_risk = get_population_in_radius(
            lat=request.impact_lat, lng=request.impact_lng, radius_km=final_radius_km
        )
        economic_impact_usd = get_economic_impact(population_in_risk)
        print(" -> Geography OK!")

        print("Step E: Generating report...")
        llm_report = f"AI Report: Impact simulated. PHA risk predicted: {final_pha_risk} (Source: {risk_source}). Energy: {physics_results['energia_megatons']} MT. Final damage: {final_radius_km} km, affecting an estimated population of {population_in_risk} people, with an estimated economic impact of ${economic_impact_usd:,.0f} USD."
        print(" -> Report OK!")

        response = SimulationResponse(
            kpis={
                "population_in_risk": population_in_risk,
                "impacto_economico_usd": economic_impact_usd,
                "impact_energy_megatons": physics_results['energia_megatons'],
                "final_damage_radius_km": final_radius_km,
                "is_pha_prediction": final_pha_risk,
                "risk_assessment_source": risk_source
            },
            details={
                "input_params": request.dict(),
                "scenario_params": scenario_params,
                "physics_output": physics_results,
                "llm_report": llm_report
            }
        )
        
        print("--- SIMULATION COMPLETED SUCCESSFULLY ---")
        return response

    except Exception as e:
        print(f"!!! ERROR DURING SIMULATION: {e} !!!")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"An internal server error occurred: {e}")
    

@router.post("/ask-agent", response_model=str, tags=["Agent"])
async def ask_agent(request: ChatRequest):
    """
    Chatbot endpoint. Receives a question and simulation context.
    """
    try:
        if not gemini_model:
            raise HTTPException(status_code=500, detail="AI model not configured.")

        prompt = f"You are an expert assistant in asteroids and planetary defense. Answer the user's question clearly and educationally. Current simulation context: {request.context}. User question: {request.question}"
        
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI agent error: {e}")