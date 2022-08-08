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
