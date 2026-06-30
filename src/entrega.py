TAXA_FIXA = 5
LIMITE_KM_TAXA_FIXA = 3
VALOR_POR_KM_EXCEDENTE = 1.5

def calcular_taxa_entrega(distancia_km):
    _validar_distancia(distancia_km)

    if distancia_km <= LIMITE_KM_TAXA_FIXA:
        return TAXA_FIXA
    
    return TAXA_FIXA + _calcular_valor_excedente(distancia_km)

def _validar_distancia(distancia_km):
    if distancia_km < 0:
        raise ValueError("Distância inválida")


def _calcular_valor_excedente(distancia_km):
    km_excedente = distancia_km - LIMITE_KM_TAXA_FIXA
    return km_excedente * VALOR_POR_KM_EXCEDENTE