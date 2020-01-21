from task_a import run_sequence


if __name__ == '__main__':
    # Using the functions written in a because duplicated code is not nice
    value_n = ''

    while not value_n.isnumeric():
        value_n = input("Please enter a positive integer Number n: \t")

    for value_m in range(1, 10001):
        print("Steps required for m - %s : %s" % (value_m, run_sequence(value_m, int(value_n))))
