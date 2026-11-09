import pytest
from identifier import Identifier

@pytest.fixture
def identifier():
    return Identifier()

def test_empty_string(identifier):
    """Testa o limite inferior inválido (string vazia -> length = 0)"""
    with pytest.raises(IndexError):
        identifier.validate_identifier("")

@pytest.mark.parametrize("input_str, expected", [
    # Particionamento de Equivalência e Valores Limítrofes para Comprimento (1 a 5)
    ("A", True),       # Comprimento 1 (Limite inferior exato)
    ("Ab", True),      # Comprimento 2 (Válido)
    ("Abcde", True),   # Comprimento 5 (Limite superior exato)
    ("Abcdef", False), # Comprimento 6 (Acima do limite superior - Inválido)
    
    # Validação do primeiro caractere (valid_s)
    ("z", True),       # Letra minúscula válida no início
    ("1A", False),     # Dígito no início (Inválido)
    ("#A", False),     # Caractere especial no início (Inválido)

    # Validação de caracteres intermediários (valid_f)
    ("A1b", True),     # Dígito no meio (Válido)
    ("A#b", False),    # Caractere especial no meio (Inválido)

    # Limites da tabela ASCII para caracteres iniciais/gerais
    ("@", False),      # Caractere imediatamente anterior a 'A' (ASCII 64)
    ("A", True),       # 'A' (ASCII 65 - Limite inferior)
    ("Z", True),       # 'Z' (ASCII 90 - Limite superior)
    ("[", False),      # Caractere imediatamente posterior a 'Z' (ASCII 91)
    ("`", False),      # Caractere imediatamente anterior a 'a' (ASCII 96)
    ("a", True),       # 'a' (ASCII 97 - Limite inferior)
    ("z", True),       # 'z' (ASCII 122 - Limite superior)
    ("{", False)       # Caractere imediatamente posterior a 'z' (ASCII 123)
])
def test_identifier_scenarios(identifier, input_str, expected):
    assert identifier.validate_identifier(input_str) == expected