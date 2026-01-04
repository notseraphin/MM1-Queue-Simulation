import numpy as np

def empirical_stationary_distribution(queue_lengths, max_state):
    counts = np.zeros(max_state + 1)
    for n in queue_lengths:
        if n <= max_state:
            counts[n] += 1
    return counts / counts.sum()


def theoretical_stationary_distribution(rho, max_state):
    return np.array([(1 - rho) * rho**n for n in range(max_state + 1)])


def average_queue_length(queue_lengths):
    return np.mean(queue_lengths)

def time_average_queue_length(states, times):
    states = np.array(states)
    times = np.array(times)
    return np.sum(states * times) / np.sum(times)