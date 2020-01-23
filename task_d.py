import matplotlib as plt

from task_a import run_sequence

if __name__ == '__main__':
    m_values = range(0, 10001)

    steps = [run_sequence(m) for m in m_values]

    plt.plot(steps)
    plt.show()

