import numpy as np

class MM1Queue:
    def __init__(self, lambda_rate, mu_rate, seed=None):
        self.lambda_rate = lambda_rate
        self.mu_rate = mu_rate
        self.rng = np.random.default_rng(seed)

        # Simulation bookkeeping
        self.queue_length = 0
        self.last_event_time = 0.0
        self.states = []  # store previous queue length
        self.times = []   # store duration spent in previous queue length

    def simulate(self, T):
        """Simulate M/M/1 queue up to time T."""
        t = 0.0
        n = 0  # current queue length

        next_arrival = self.rng.exponential(1 / self.lambda_rate)
        next_departure = np.inf

        self.queue_length = n
        self.last_event_time = 0.0
        self.states = []
        self.times = []

        while t < T:
            if next_arrival < next_departure:
                t = next_arrival
                # record time spent in current state
                self.states.append(self.queue_length)
                self.times.append(t - self.last_event_time)
                self.last_event_time = t

                n += 1
                self.queue_length = n

                next_arrival = t + self.rng.exponential(1 / self.lambda_rate)
                if n == 1:
                    next_departure = t + self.rng.exponential(1 / self.mu_rate)
            else:
                t = next_departure
                # record time spent in current state
                self.states.append(self.queue_length)
                self.times.append(t - self.last_event_time)
                self.last_event_time = t

                n -= 1
                self.queue_length = n

                if n > 0:
                    next_departure = t + self.rng.exponential(1 / self.mu_rate)
                else:
                    next_departure = np.inf

        return np.array(self.states), np.array(self.times)
