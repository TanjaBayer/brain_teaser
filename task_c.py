from pytictoc import TicToc
from joblib import Parallel, delayed


from task_a import calc_sequence, run_sequence


def run_sequence_with_buffer(m, buffer):
    """ Run the sequence but store the start value and the steps required in a buffer

    This buffer can be used further steps to stop the processing when the value is reached,
    because the required steps are than already known

    Args:
        m: start value of the sequence
        buffer: the buffer for storing the value, step pairs

    Returns:
        the steps require to reach 1 for the first time
    """
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
    m_values = range(1, 10001)
    timer = TicToc()

    # Calculate time of the calculation of step b
    timer.tic()  # Start the timer
    [run_sequence(m) for m in m_values]
    print("Time for calulation of task b: %s" % timer.tocvalue())  # Stop the timer and store value

    # Run the same job in parallel on multiple cpus, normaly that should minimize the normal
    # calculation time, but in this case it seams to generate more overhead
    timer.tic()
    arr = Parallel(n_jobs=-1)(delayed(run_sequence)(m) for m in m_values)
    print("Time for calulation of task b with parallel jobs: %s" % timer.tocvalue())

    # Store already known sequence and number of steps in a buffer which can be used in later steps
    timer.tic()  # Start the timer
    buffer = {}
    [run_sequence_with_buffer(m, buffer) for m in m_values]
    print("Time for calulation of improved version: %s" % timer.tocvalue())  # Stop the timer and
    # store value

    # Try parallel jobs for speedup implementation
    timer.tic()
    Parallel(n_jobs=-1, require="sharedmem")(delayed(run_sequence_with_buffer)(m, buffer) for m
                                               in m_values)
    print("Time for calulation of improved version with parallel jobs: %s" % timer.tocvalue())
