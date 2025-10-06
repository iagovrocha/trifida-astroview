import numpy as np
import joblib
import pandas as pd
import warnings

# Suppress scikit-learn version warnings for pre-trained models
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

MODEL_PATH = "ml_models/pha_classifier.pkl"
PHA_CLASSIFIER_MODEL = joblib.load(MODEL_PATH)


def predict_pha_risk(features_dict: dict) -> bool:
    """
    Usa o modelo carregado para prever se um asteroide é um PHA.
    """
    # O modelo espera as colunas na mesma ordem do treinamento
    features_order = [
        'absolute_magnitude_h', 'diameter_km_avg', 'velocity_km_s',
        'miss_distance_km', 'kinetic_energy_joules'
    ]
    
    # Cria um DataFrame de uma linha com os dados da simulação
    input_df = pd.DataFrame([features_dict], columns=features_order)
    
    # Faz a predição
    prediction = PHA_CLASSIFIER_MODEL.predict(input_df)
    
    return bool(prediction[0])


def calculate_damage_from_pair_model(
    diameter_km: float, 
    velocity_km_s: float, 
    impact_angle: float,
    densidade_rho: float,
    eficiencia_eta: float
    ) -> dict:
    """
    Calcula as consequências de um impacto usando as equações do modelo PAIR.
    """
    
    # 1. Calcular Energia de Impacto (E)
    # Primeiro, convertemos tudo para unidades do SI (metros, kg, segundos)
    raio_m = (diameter_km * 1000) / 2
    velocidade_m_s = velocity_km_s * 1000
    
    # Volume (assumindo uma esfera) e Massa
    volume_m3 = (4/3) * np.pi * (raio_m ** 3)
    massa_kg = densidade_rho * volume_m3
    
    # Energia Cinética em Joules, corrigida pelo ângulo de entrada
    energia_cinetica_j = 0.5 * massa_kg * (velocidade_m_s ** 2) * np.sin(np.radians(impact_angle))
    
    # Converter para Megatons de TNT (1 MT = 4.184e15 Joules) para usar nas equações de dano
    energia_E_megatons = energia_cinetica_j / 4.184e15

    # 2. Simplificar Altitude de Explosão (h)
    # Para o hackathon, usamos uma regra simples: objetos pequenos explodem no ar.
    if diameter_km < 0.05: # Menos de 50 metros
        altitude_h_km = 5.0 # Assume explosão a 5km de altitude (airburst)
    else:
        altitude_h_km = 0.0 # Assume impacto direto no solo

    # 3. Calcular Raio de Dano por Explosão (Blast Overpressure)
    E = energia_E_megatons
    h = altitude_h_km
    
    if h > 0: # Se for um airburst
        raio_blast_km = (2.09 * (h**-0.449) * (h**2) * (E**(-1/3))) + (5.08 * (E**(1/3)))
    else: # Se for impacto no solo
        raio_blast_km = 5.08 * (E**(1/3))

    # 4. Calcular Raio de Dano Térmico
    eta = eficiencia_eta
    Zi = 0.42 * (E**(1/6))
    r_sq = (eta * E) / (2 * np.pi * Zi)
    h_sq = h**2
    
    raio_thermal_km = np.sqrt(r_sq - h_sq) if r_sq > h_sq else 0.0
    
    # 5. Montar o dicionário de resultados da física
    results = {
        "energia_megatons": round(E, 2),
        "altitude_explosao_km": round(h, 2),
        "raio_dano_explosao_km": round(raio_blast_km, 2),
        "raio_dano_termico_km": round(raio_thermal_km, 2),
        "raio_dano_final_km": round(max(raio_blast_km, raio_thermal_km), 2),
        "kinetic_energy_joules": energia_cinetica_j # Guardamos para usar na IA
    }
    
    return results