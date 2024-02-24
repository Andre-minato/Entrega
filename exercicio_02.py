import pytest

def valor_com_desconto(vlr_produto):
    desconto = (vlr_produto / 100) * 9
    vlr_com_desconto = vlr_produto - desconto
    return vlr_com_desconto, desconto

def test_valor_desconto_case_01():
    assert valor_com_desconto(100) == (91.00, 9.00)

def test_valor_desconto_case_02():
    assert valor_com_desconto(1500) == (1365.00, 135.00)

def test_valor_desconto_case_03():
    assert valor_com_desconto(60000) == pytest.approx((54600.00, 5400.00), 0.01)