import pytest

from task_a import calc_sequence, run_sequence


@pytest.mark.parametrize("m", [1, 1000, 50])
def test_cm_is_m_for_cm_of_1(m):
    assert calc_sequence(m, None) == m


@pytest.mark.parametrize("m, old_val, result", [('*', 3, 10), ('`*', 9, 28), ('*', 100001, 300004)])
def test_cm_is_multiplied_by_3_summed_with_1_for_uneven_values_of_cm(m, old_val, result):
    assert calc_sequence(m, old_val) == result


@pytest.mark.parametrize("m, old_val, result", [('*', 2, 1), ('*', 200, 100), ('*', 28558, 14279)])
def test_cm_is_devided_by_two_for_even_values_of_cm(m, old_val, result):
    assert calc_sequence(m, old_val) == result


@pytest.mark.parametrize("m, result", [(1, 1), (5, 6), (20, 8), (800, 29)])
def test_run_sequence_returns_correct_value_for_steps(m, result):
    assert run_sequence(m) == result
