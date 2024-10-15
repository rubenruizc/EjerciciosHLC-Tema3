from cambio import change

def test_cambio1():
    assert change('a',5) == 'f'

def test_cambio2():
    assert change('h',5) == 'm'

def test_cambio3():
    assert change('b',1) == 'c'

def test_cambio4():
    assert change('d',2) == 'f'

def test_cambio5():
    assert change('ab',1) == 'bc'

def test_cambio6():
    assert change('z',1) == 'a'


