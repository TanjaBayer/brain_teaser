
def calc_sequence(m, old_val):
    if not old_val:
        return m
    if old_val % 2:
        return old_val * 3 + 1
    return old_val/2


def run_sequence(m):
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




