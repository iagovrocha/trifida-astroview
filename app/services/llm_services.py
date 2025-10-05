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

    # Formata os dados da simulação numa string legível para a IA (igual a antes)
    data_summary = f"""
    - Local do Impacto: Lat {input_params['impact_lat']}, Lng {input_params['impact_lng']}
    - Tipo de Asteroide: {input_params['asteroid_type']}
    - Diâmetro: {input_params['diameter_km']} km
    - Velocidade: {input_params['velocity_km_s']} km/s
    - Energia do Impacto: {simulation_results['energia_megatons']} Megatons
    - Raio de Dano Final: {simulation_results['raio_dano_final_km']} km
    - Classificação de Risco (IA+Física): {simulation_results['is_pha_prediction']}
    - População Afetada Estimada: {simulation_results.get('population_in_risk', 'N/A')}
    - Impacto Económico Estimado: ${simulation_results.get('impacto_economico_usd', 0):,.0f} USD
    """

    # O Prompt: As instruções para o nosso agente de IA (igual a antes)
    prompt = f"""
    Você é um Analista de Risco Sênior da Divisão de Defesa Planetária da NASA.
    Você acaba de receber os dados de uma simulação de impacto de asteroide e precisa de escrever um briefing de emergência claro e conciso para decisores governamentais.

    Dados da Simulação:
    {data_summary}

    Sua Tarefa:
    Escreva um briefing de emergência. Use um tom sério e direto.
    Estruture a sua resposta em três secções, usando Markdown para formatação:

    ### 1. SUMÁRIO DO IMPACTO
    (Descreva o evento em 1-2 frases. Qual a escala do impacto?)

    ### 2. ANÁLISE DE RISCOS
    (Detalhe as principais consequências, focando nos dados fornecidos:
    - Risco Humanitário: Fale sobre a população afetada.
    - Risco Económico: Fale sobre os danos estimados.
    - Risco Geográfico: Descreva a área de dano.)

    ### 3. RECOMENDAÇÕES PRIORITÁRIAS
    (Sugira 2-3 ações imediatas que as equipas de emergência deveriam tomar com base na análise.)
    """

    try:
        # A chamada à API do Gemini é diferente
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro ao chamar a API do Gemini: {e}")
        return "A análise de risco por IA não pôde ser gerada neste momento devido a um erro."