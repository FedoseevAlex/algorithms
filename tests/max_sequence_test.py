import pytest

from algorithms import max_sequence as ms


def test_max_seq():
    assert ms.max_seq([3, 6, 7, 12]) == 3
