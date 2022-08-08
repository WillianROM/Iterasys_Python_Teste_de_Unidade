# Bibliotecas
import pytest
from main import somar_dois_numeros

# Funções teste de unidade
def test_somar_dois_numeros():
    # 1 - Configura
        # 1.1 - Dados de Entrada
    numeroA = 7
    numeroB = 5

        # 1.2 - Resultados Esperados
    resultado_esperado = 12

    # 2 - Executa
    resultado_obtido = somar_dois_numeros(numeroA, numeroB)

    # 3 - Válida
    assert resultado_obtido == resultado_esperado



#Segundo Teste com lista de Valores
lista_para_somar = {
    (5, 9, 14),
    (10, -4, 6),
    (4, 0, 4)
}

@pytest.mark.parametrize('numeroA, numeroB, resultado_esperado', lista_para_somar)
def teste_somar_dois_numeros_da_Lista(numeroA, numeroB, resultado_esperado):
    # 1 - Configura
        # 1.1 - Dados de Entrada (Valores vem da lista)
        # 1.2 - Resultados Esperados (Valores vem da lista)

    # 2 - Executa
    resultado_obtido = somar_dois_numeros(numeroA, numeroB)

    # 3 - Válida
    assert resultado_obtido == resultado_esperado
