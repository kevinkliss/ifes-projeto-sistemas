from calculadora import operacoes

def test_somar():
    assert operacoes.somar(2, 3) == 5

def test_subtrair():
    assert operacoes.subtrair(10, 4) == 6

def test_multiplicar():
    assert operacoes.multiplicar(3, 7) == 21

def test_dividir():
    assert operacoes.dividir(10, 2) == 5

def test_divisao_por_zero():
    assert operacoes.dividir(10, 0) == "Não é possível dividir por 0."
