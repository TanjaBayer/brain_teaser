
def calc_sequence(m, n, old_val):
    if n == 1:
        return m
    if not old_val:
        old_val = calc_sequence(m, n - 1, None)
    if old_val % 2:
        return old_val * 3 + 1
    return old_val/2


def run_sequence(m, n):
    result = None
    start_val = n
    while result != 1:
        result = calc_sequence(m, n, result)
        n += 1

    return n - start_val - 1



if __name__ == '__main__':
    # assuming we should calculate the steps for a single but not fixed value of m and a variable n
    # reading in from terminal

    value_m = ''
    value_n = ''

    while not value_m.isnumeric():
        value_m = input("Please enter a positive integer Number m: \t")

    while not value_n.isnumeric():
        value_n = input("Please enter a positive integer Number n: \t")

    print("Steps required %s" % run_sequence(int(value_m), int(value_n)))




