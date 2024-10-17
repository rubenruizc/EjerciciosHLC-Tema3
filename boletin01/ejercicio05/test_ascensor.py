from ascensor import recorrido

def test_recorrido1():
    assert recorrido('5 4') == 1

def test_recorrido2():
    assert recorrido('5 4 7 1') == 10

def test_recorrido3():
    assert recorrido('5') == 0

def test_recorrido4():
    assert recorrido('0 1 5 2 0 3 9') == 19

def test_recorrido5():
    assert recorrido('5 5 4') == 1

def test_recorrido6():
    assert recorrido('1 2 3 4 5') == 4

def test_recorrido7():
    assert recorrido("1 2") == 1
