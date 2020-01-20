import pytest

from ..task_a import calc_sequence


@pytest.mark.parametrize("m, n", [(1, 1), (1000, 1), (50, 1)])
def test_cm_is_m_for_cm_of_1(m, n):
    
    calc_sequence(m, n)
