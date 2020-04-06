import pytest

from algorithms import inversions as inv

test_data = [([1, 2, 3, 5, 4], 1), ([2, 3, 9, 2, 9], 2), ([7, 6, 5, 4, 3, 2, 1], 21)]


@pytest.mark.parametrize("array,control", test_data)
def test_inversions(array, control):
    inversions, res = inv.get_inversions(array)
    print(res)
    assert inversions == control
