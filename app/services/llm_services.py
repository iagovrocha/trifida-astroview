import google.generativeai as genai
from app.core import config

# Configura o cliente do Gemini com a sua chave de API
try:
    genai.configure(api_key=config.GOOGLE_API_KEY)
    # Inicializa o modelo que vamos usar
    gemini_model = genai.GenerativeModel("gemini-2.0-flash")
    print("Modelo Gemini ('gemini-pro') configurado com sucesso.")
except Exception as e:
    print(f"Erro ao configurar a API do Gemini: {e}")
    gemini_model = None


def generate_llm_report(simulation_results: dict, input_params: dict) -> str:
    """
    Gera um relatório de análise de risco usando o modelo Gemini do Google.
    """
    if not gemini_model:
        return "A análise de risco por IA não está disponível (erro de configuração)."

    # Format simulation data in a readable string for the AI
    data_summary = f"""
    - Impact Location: Lat {input_params['impact_lat']}, Lng {input_params['impact_lng']}
    - Asteroid Type: {input_params['asteroid_type']}
    - Diameter: {input_params['diameter_km']} km
    - Velocity: {input_params['velocity_km_s']} km/s
    - Impact Energy: {simulation_results['energia_megatons']} Megatons
    - Final Damage Radius: {simulation_results['raio_dano_final_km']} km
    - Risk Classification (AI+Physics): {simulation_results['is_pha_prediction']}
    - Estimated Affected Population: {simulation_results.get('population_in_risk', 'N/A')}
    - Estimated Economic Impact: ${simulation_results.get('impacto_economico_usd', 0):,.0f} USD
    """

    # The Prompt: Instructions for our AI agent
    prompt = f"""
    You are a Senior Risk Analyst for NASA's Planetary Defense Division.
    You have just received data from an asteroid impact simulation and need to write a clear and concise emergency briefing for government decision-makers.

    Simulation Data:
    {data_summary}

    Your Task:
    Write an emergency briefing. Use a serious and direct tone.
    Structure your response in three sections, using Markdown formatting:

    ### 1. IMPACT SUMMARY
    (Describe the event in 1-2 sentences. What is the scale of the impact?)

    ### 2. RISK ANALYSIS
    (Detail the main consequences, focusing on the provided data:
    - Humanitarian Risk: Discuss the affected population.
    - Economic Risk: Discuss the estimated damages.
    - Geographic Risk: Describe the damage area.)

    ### 3. PRIORITY RECOMMENDATIONS
    (Suggest 2-3 immediate actions that emergency teams should take based on the analysis.)
    """

    try:
        # A chamada à API do Gemini é diferente
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro ao chamar a API do Gemini: {e}")
        return "A análise de risco por IA não pôde ser gerada neste momento devido a um erro."