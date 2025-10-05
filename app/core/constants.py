GCM3_TO_KGM3 = 1000  # Converte de g/cm^3 para kg/m^3
MPA_TO_PA = 1e6      # Converte de Megapascals para Pascals

SCENARIOS = {
    "Cometa": {
        "description": "Um corpo composto principalmente de gelo e poeira, com baixa densidade e baixa resistência. Tende a se fragmentar facilmente na atmosfera.",
        
        "densidade_rho": 1.1 * GCM3_TO_KGM3,    # kg/m^3
        "resistencia_s": 0.1 * MPA_TO_PA,     # Pascals (Pa)
        "eficiencia_eta": 0.003                 # Adimensional (valor alto na faixa, pois voláteis brilham mais)
    },
    
    "Rochoso": {
        "description": "Um asteroide rochoso, com densidade e resistência intermediárias. O tipo mais comum de objeto próximo à Terra.",
        
        "densidade_rho": 3.0 * GCM3_TO_KGM3,    # kg/m^3
        "resistencia_s": 5.0 * MPA_TO_PA,     # Pascals (Pa)
        "eficiencia_eta": 0.001                 # Adimensional (valor médio na faixa)
    },
    
    "Metálico": {
        "description": "Um asteroide denso e coeso, composto principalmente de ferro e níquel. É muito resistente e penetra mais fundo na atmosfera.",
        
        "densidade_rho": 7.5 * GCM3_TO_KGM3,    # kg/m^3
        "resistencia_s": 10.0 * MPA_TO_PA,    # Pascals (Pa)
        "eficiencia_eta": 0.0005                # Adimensional (valor baixo na faixa)
    }
}

CATASTROPHIC_THRESHOLD_MT = 500 # Megatons