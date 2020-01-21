
def calc_sequence(m, n, old_val):
    if n == 1:
        return m
    if old_val % 2:
        return old_val * 3 + 1

