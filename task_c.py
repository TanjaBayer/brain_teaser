from pytictoc import TicToc

from .task_a import calc_sequence, run_sequence


def run_sequence_with_buffer(m, buffer):
    result = calc_sequence(m, None)
    old_val = None
    n = 1

    while old_val != 1:
        if old_val in buffer:
            n += buffer[old_val] - 1
            break
        old_val = calc_sequence(m, old_val)
        n += 1

    buffer[result] = n-1

    return n - 1


if __name__ == '__main__':
    # Using the functions written in task_a because duplicated code is not nice ;)
    timer = TicToc()

    timer.tic()  # Start the timer
    for value_m in range(1, 10001):
        print("Steps required for m - %s : %s" % (value_m, run_sequence(value_m)))
    time_b = timer.tocvalue()  # Stop the timer and store value

    timer.tic()  # Start the timer
    buffer = {}
    for value_m in range(1, 10001):
        print("Steps required for m - %s : %s" % (value_m, run_sequence_with_buffer(value_m, buffer)))

    time_c = timer.tocvalue()  # Stop the timer and store value

    print("Time for version from task b: % and task_c %s" % (time_b, time_c))

    if time_c < time_b:
        print("Success calculation time improved")