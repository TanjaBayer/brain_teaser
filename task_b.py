from task_a import run_sequence


if __name__ == '__main__':
    # Using the functions written in task_a because duplicated code is not nice ;)

    for value_m in range(1, 10001):
        print("Steps required for m - %s : %s" % (value_m, run_sequence(value_m)))
