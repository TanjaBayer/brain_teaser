
def calc_sequence(m, old_val):
    """ Calc the next value based on the last value and the start value

    Args:
        m:  The start value of the sequence
        old_val: The last value

    Returns:
        The new calculated value
    """
    if not old_val:
        return m
    if old_val % 2:
        return old_val * 3 + 1
    return old_val/2


def run_sequence(m):
    """ For a given m run the sequence until 1 is reached fo the first time

    Args:
        m: The start value of the sequence

    Returns:
        The steps required to reach 1 for the first time
    """
    result = None
    n = 1
    while result != 1:
        result = calc_sequence(m, result)
        n += 1

    return n - 1


if __name__ == '__main__':
    # assuming we should calculate the steps for a single but not fixed value of m and a variable n
    # reading in from terminal

    value_m = ''

    while not value_m.isnumeric():
        value_m = input("Please enter a positive integer Number m: \t")

    print("Steps required %s" % run_sequence(int(value_m)))




