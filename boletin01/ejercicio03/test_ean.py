from ean import verificar_digito_control

def test_codigo_ean1():
    assert verificar_digito_control("65839522") == True

def test_codigo_ean2():
    assert verificar_digito_control("65839521") == False

def test_codigo_ean3():
    assert verificar_digito_control("8414533043847") == True

def test_codigo_ean4():
    assert verificar_digito_control("5029365779425") == True

def test_codigo_ean5():
    assert verificar_digito_control("5129365779425") == False