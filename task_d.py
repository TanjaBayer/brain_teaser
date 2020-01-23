from pytictoc import TicToc
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


from task_a import run_sequence


if __name__ == '__main__':
    m_values = range(1, 10001)
    timer = TicToc()

    # Calculate time of the calculation of step b
    timer.tic()  # Start the timer
    steps = [run_sequence(m) for m in m_values]
    timer.toc()

    # Show it python3-tk needs to be installed
    plt.plot(steps)
    plt.show()

    # And save it
    plt.plot(steps)
    plt.savefig("digramm_task_d.png")
