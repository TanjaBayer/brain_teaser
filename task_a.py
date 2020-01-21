
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
    while result != 1:
        result = calc_sequence(m, n, result)
        n += 1
    return n - 1


if __name__ == '__main__':
    pass