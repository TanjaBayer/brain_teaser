import pytest

from ..task_a import calc_sequence, run_sequence


@pytest.mark.parametrize("m, n", [(1, 1), (1000, 1), (50, 1)])
def test_cm_is_m_for_cm_of_1(m, n):
    calc_sequence(m, n, 0)


@pytest.mark.parametrize("m, n, result", [(5, 2, 16), (11, 2, 34), (1000001, 2, 3000004)])
def test_cm_is_multiplied_by_3_summed_with_1_for_uneven_values_of_cm(m, n, result):
    assert calc_sequence(m, n, m) == result


@pytest.mark.parametrize("m, n, result", [(2, 2, 1), (80, 2, 40), (80006, 2, 40003)])
def test_cm_is_devided_by_two_for_even_values_of_cm(m, n, result):
    assert calc_sequence(m, n, m) == result


@pytest.mark.parametrize("m, n, result", [(1, 1, 1), (5, 1, 6), (20, 5, 8)])
def test_run_sequence_retruns_correct_value_for_steps(m, n, result):
    assert run_sequence(m, n) == result


@pytest.mark.parametrize("m, n, result", [(2, 2, 1), (20, 5, 8), (13, 7, 8)])
def test_calc_sequence_if_not_starting_with_n_equals_1(m, n, result):
    assert calc_sequence(m, n, None) == result