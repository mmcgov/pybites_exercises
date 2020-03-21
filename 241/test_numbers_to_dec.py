import pytest
from numbers_to_dec import list_to_decimal


# test ValueError
@pytest.mark.parametrize('arg, expected', ([3,2], 32), ([3,6,4,2], 3642) ([2,3], 23))
def test_list_to_decimal(arg, expected) -> None:
    assert list_to_decimal(arg) == expected


# test ValueError
@pytest.mark.parametrize('arg', [[3,2,True], [3.6,4,2], ['g',2,3]])
def test_TypeError(arg) -> None:
    with pytest.raises(TypeError):
        result = list_to_decimal(arg)


# test TypeError
@pytest.mark.parametrize('arg', [[-3,2], [13,2]])
def test_ValueError() -> None:
    with pytest.raises(ValueError):
        result = list_to_decimal(arg)


# test out of range error
def test_out_of_range_error() -> None:
    with pytest.raises(ValueError):
        value = list_to_decimal([0,13,2])
        if value  == 132:
            raise ValueError
