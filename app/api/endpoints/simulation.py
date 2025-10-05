from fastapi import APIRouter, HTTPException
from app.models.simulation import SimulationRequest, SimulationResponse
from app.core.constants import SCENARIOS, CATASTROPHIC_THRESHOLD_MT
import google.generativeai as genai
from app.models.simulation import ChatRequest
from app.services.simulation_engine import calculate_damage_from_pair_model, predict_pha_risk
from app.services.geo_analysis import get_population_in_radius, get_economic_impact
from app.services.llm_services import gemini_model

router = APIRouter()

@router.post("/simulate", response_model=SimulationResponse)
async def run_synchronous_simulation(request: SimulationRequest):
    """
    Executa a simulação completa (física, IA, geolocalização) e retorna 
    um objeto estruturado com KPIs e detalhes.
    """
    print(f"--- INICIANDO NOVA SIMULAÇÃO ---")
    print(f"Input do utilizador: {request.dict()}")

    try:
        print("Passo A: A executar cálculos de física...")
        asteroid_type = request.asteroid_type
        if asteroid_type not in SCENARIOS:
            raise HTTPException(status_code=400, detail=f"Tipo de asteroide inválido: {asteroid_type}")
        
        scenario_params = SCENARIOS.get(asteroid_type)
        engine_args = {
            "diameter_km": request.diameter_km,
            "velocity_km_s": request.velocity_km_s,
            "impact_angle": request.impact_angle,
            "densidade_rho": scenario_params["densidade_rho"],
            "eficiencia_eta": scenario_params["eficiencia_eta"]
        }
        physics_results = calculate_damage_from_pair_model(**engine_args)
        print(" -> Física OK!")

        print("Passo B: A executar predição de IA...")
        ml_features = {
            'absolute_magnitude_h': 22.0, 'diameter_km_avg': request.diameter_km,
            'velocity_km_s': request.velocity_km_s, 'miss_distance_km': 10000000,
            'kinetic_energy_joules': physics_results['kinetic_energy_joules']
        }
        pha_prediction = predict_pha_risk(ml_features)
        print(" -> IA OK!")

        print("Passo D: A aplicar regra de segurança...")
        final_pha_risk = pha_prediction
        risk_source = "Machine Learning"

        if physics_results['energia_megatons'] > CATASTROPHIC_THRESHOLD_MT:
            final_pha_risk = True
            risk_source = "Regra de Segurança de Física"
        print(" -> Análise de Risco OK!")

        print("Passo C: A calcular impacto geográfico...")
        final_radius_km = physics_results['raio_dano_final_km']
        population_in_risk = get_population_in_radius(
            lat=request.impact_lat, lng=request.impact_lng, radius_km=final_radius_km
        )
        economic_impact_usd = get_economic_impact(population_in_risk)
        print(" -> Geografia OK!")

        print("Passo E: A gerar relatório...")
        llm_report = f"Relatório de IA: Impacto simulado. Risco de PHA previsto: {final_pha_risk} (Fonte: {risk_source}). Energia: {physics_results['energia_megatons']} MT. Dano final: {final_radius_km} km, afetando uma população estimada de {population_in_risk} pessoas, com um impacto económico estimado de ${economic_impact_usd:,.0f} USD."
        print(" -> Relatório OK!")

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
        
        print("--- SIMULAÇÃO CONCLUÍDA COM SUCESSO ---")
        return response

    except Exception as e:
        print(f"!!! ERRO DURANTE A SIMULAÇÃO: {e} !!!")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro interno no servidor: {e}")
    

@router.post("/ask-agent", response_model=str, tags=["Agent"])
async def ask_agent(request: ChatRequest):
    """
    Endpoint para o chatbot. Recebe uma pergunta e o contexto da simulação.
    """
    try:
        if not gemini_model:
            raise HTTPException(status_code=500, detail="Modelo de IA não configurado.")

        prompt = f"Você é um assistente especialista em asteroides e defesa planetária. Responda à pergunta do utilizador de forma clara e educativa. Contexto da simulação atual: {request.context}. Pergunta do utilizador: {request.question}"
        
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no agente de IA: {e}")