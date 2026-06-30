from entrega import calcular_taxa_entrega
import pytest

def test_deve_retornar_taxa_fixa_para_distancia_ate_3km():
    resultado = calcular_taxa_entrega(2)
    assert resultado == 5

def test_deve_cobrar_taxa_proporcional_para_distancia_acima_de_3km():
    resultado = calcular_taxa_entrega(5)
    assert resultado == 8

def test_deve_lancar_erro_quando_distancia_for_negativa():
    with pytest.raises(ValueError, match="Distância inválida"):
        calcular_taxa_entrega(-1)