import pytest

from ..task_a import calc_sequence


@pytest.mark.parametrize("m, n", [(1, 1), (1000, 1), (50, 1)])
def test_cm_is_m_for_cm_of_1(m, n):
    calc_sequence(m, n, 0)


@pytest.mark.parametrize("m, n, result", [(5, 2, 16), (11, 2, 34), (1000001, 2, 3000004)])
def test_cm_is_multiplied_by_3_summed_with_1_for_uneven_values_of_cm(m, n, result):
    assert calc_sequence(m, n, m) == result


@pytest.mark.parametrize("m, n, result", [(2, 2, 1), (80, 2, 40), (80006, 2, 40003)])
def test_cm_is_devided_by_two_for_even_values_of_cm(m, n, result):
    assert calc_sequence(m, n, m) == result
