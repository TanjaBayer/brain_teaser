import pytest

from task_a import run_sequence
from task_c import run_sequence_with_buffer


@pytest.mark.parametrize('m', [1, 2, 3, 100, 10000])
def test_run_sequence_and_run_sequence_buffer_return_same_val(m):
    buffer = {}
    assert run_sequence(m) == run_sequence_with_buffer(m, buffer)