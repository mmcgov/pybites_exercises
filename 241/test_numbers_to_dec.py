import pytest
from numbers_to_dec import list_to_decimal

# test ValueError
def test_list_to_decimal_ValueError() -> None:
    with pytest.raises(ValueError):
        assert list_to_decimal(-1) == 1

# test TypeError
def test_list_to_decimal_ValueError() -> None:
    with pytest.raises(TypeError):
        assert list_to_decimal(-1.5) == 1
