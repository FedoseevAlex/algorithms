import pytest

from algorithms import inversions as inv

test_data = [
    ([2, 3, 9, 2, 9], 2)
]

@pytest.mark.parametrize("array,control", test_data)
def test_inversions(array, control):
    assert inv.get_inversions(array) == control
