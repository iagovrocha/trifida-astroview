GCM3_TO_KGM3 = 1000  # Converte de g/cm^3 para kg/m^3
MPA_TO_PA = 1e6      # Converte de Megapascals para Pascals

# Mapping from English to Portuguese asteroid type names (keeping English names as primary)
ASTEROID_TYPE_MAPPING = {
    "Sedimentary Rock": "Sedimentary Rock",
    "Water": "Water", 
    "Crystalline Rock": "Crystalline Rock"
}

SCENARIOS = {
    "Sedimentary Rock": {
        "description": "Um asteroide composto por rochas sedimentares, formado pela compactação de sedimentos ao longo do tempo. Possui densidade moderada e estrutura relativamente frágil.",
        
        "densidade_rho": 2.5 * GCM3_TO_KGM3,    # kg/m^3 (densidade moderada)
        "resistencia_s": 3.0 * MPA_TO_PA,       # Pascals (Pa) (resistência baixa-moderada)
        "eficiencia_eta": 0.0012                # Adimensional (eficiência moderada)
    },
    
    "Water": {
        "description": "Um corpo celeste composto principalmente de gelo de água, com densidade muito baixa e resistência mínima. Altamente volátil e tende a vaporizar rapidamente na atmosfera.",
        
        "densidade_rho": 0.9 * GCM3_TO_KGM3,    # kg/m^3 (densidade do gelo)
        "resistencia_s": 0.05 * MPA_TO_PA,      # Pascals (Pa) (resistência muito baixa)
        "eficiencia_eta": 0.004                 # Adimensional (alta eficiência devido à vaporização)
    },
    
    "Crystalline Rock": {
        "description": "Um asteroide composto por minerais cristalinos bem formados, com alta densidade e resistência estrutural elevada. Estrutura interna ordenada e coesa.",
        
        "densidade_rho": 3.8 * GCM3_TO_KGM3,    # kg/m^3 (densidade alta)
        "resistencia_s": 8.0 * MPA_TO_PA,       # Pascals (Pa) (alta resistência)
        "eficiencia_eta": 0.0008                # Adimensional (baixa eficiência, penetra mais)
    }
}

CATASTROPHIC_THRESHOLD_MT = 500 # Megatons