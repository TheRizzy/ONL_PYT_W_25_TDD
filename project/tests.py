import pytest

from functions import div


def test_div_by_int():
    assert div(6, 3) == 2


def test_div_by_float():
    assert str(div(5.4, 2.2))[:10] == "2.45454545"


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


def test_div_by_str():
    with pytest.raises(TypeError):
        div("8", "4")
