import pytest
def calc_gorjeta(vlr_despesa):
    vlr_gorjeta = (vlr_despesa / 100) * 10
    vlr_total_conta = vlr_despesa + vlr_gorjeta
    return vlr_total_conta, vlr_gorjeta

def test_calc_gorjeta_case_01():
    assert calc_gorjeta(75.00) == (82.50, 7.5)

def test_calc_gorjeta_case_02():
    assert calc_gorjeta(125) == (137.50, 12.5)

def test_calc_gorjeta_case_03():
    assert calc_gorjeta(350.87) == pytest.approx((385.96, 35.09), 0.01)