import time

import pytest

from task_a import run_sequence
from task_c import run_sequence_with_buffer


@pytest.mark.parametrize('m', [1, 2, 3, 100, 10000])
def test_run_sequence_and_run_sequence_buffer_return_same_val(m):
    buffer = {}
    assert run_sequence(m) == run_sequence_with_buffer(m, buffer)


def test_new_implementation_should_be_faster_than_old_one():
    t = time.time()
    [run_sequence(m,) for m in range(1, 10001)]
    diff_old = time.time() - t

    t = time.time()
    buffer = {}
    [run_sequence_with_buffer(m, buffer) for m in range(1,10001)]
    diff_new = time.time() - t
    assert diff_new < diff_old
