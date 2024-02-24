def calc_promocao(vlr_original, vlr_desconto):
    return vlr_original - vlr_desconto

def test_calc_promocao_case_01():
    assert calc_promocao(500.0, 50.00) == (450.00)

def test_calc_promocao_case_02():
    assert calc_promocao(10500.00, 500.00) == (10000.00)

def test_calc_promocao_case_03():
    assert calc_promocao(90.00, 0.80) == (89.20)