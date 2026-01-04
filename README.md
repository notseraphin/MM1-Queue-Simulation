# MM1-Queue-Simulation

**Overview**

This project implements and analyzes an M/M/1 queue, a fundamental model in queueing theory used to describe systems such as server workloads, call centers, and network traffic.

An M/M/1 queue assumes:
- Poisson arrivals with rate λ
- Exponential service times with rate μ
- Single server
- First-come, first-served discipline

The system is modeled as a continuous-time Markov chain, and both theoretical and empirical results are studied.

**Mathematical Background**

Let
𝜌 = 𝜆/𝜇
For stability, the queue requires:
𝜌<1
Under this condition, the stationary distribution is:
𝑃(𝑁=𝑛)=(1−𝜌)p^𝑛

Key theoretical results:

- Expected queue length:
      𝐸[N]=𝜌/1−𝜌
- Expected waiting time:
      𝐸[𝑊]=1/𝜇−𝜆
  
**Project Structure**

```bash
mm1-queue-simulation/
│── src/
│   ├── queue.py        
│   ├── analysis.py   
│── notebooks/
│   └── experiments.ipynb
│── figures/
│   └── stationary_distribution.png
│── README.md
│── requirements.txt
```
**Simulation Approach**

- Arrivals and service completions are generated using exponential random variables
- The queue length process is simulated over time
- Empirical queue-length samples are collected after burn-in
- Results are compared directly against closed-form theory

**Results**

- The empirical stationary distribution converges to the theoretical geometric distribution
- The empirical expected queue length closely matches:
      𝐸[𝑁]=𝜌/1−𝜌
- This validates both the stochastic simulation and Markov chain analysis.

**Analysis**

This project implements a discrete-event simulation of an M/M/1 queue with Poisson arrivals and exponential service times. The system was simulated using arrival rate λ = 0.8 and service rate μ = 1.0, satisfying the stability condition ρ = λ / μ = 0.8 < 1. The queue was run for T = 100,000 time units to approximate steady-state behavior.

The simulation tracks exact arrival and departure events and records the time spent in each queue length state, allowing computation of time-averaged performance metrics. The empirical time-average queue length was found to be:
- Empirical E[N] ≈ 4.05
- Theoretical E[N] = ρ / (1 − ρ) = 4.00
The close agreement confirms convergence to the stationary regime and validates the correctness of the event-driven simulation.

In addition, the empirical stationary distribution of queue lengths closely matched the theoretical geometric distribution
P(N = n) = (1 − ρ)ρⁿ, further demonstrating consistency with classical queueing theory. Minor deviations are attributable to finite simulation time and sampling variability.
<img width="582" height="433" alt="image" src="https://github.com/user-attachments/assets/5cb26720-fdb1-4c27-8a70-1a99b074d7df" />

Overall, this project demonstrates how discrete-event simulation can accurately reproduce steady-state properties of Markovian queues and provides a foundation for analyzing more complex service systems where analytical solutions are intractable.

**Technologies Used**

- Python
- NumPy
- Matplotlib
- Jupyter Notebooks

**Key Takeaways**

- Demonstrates applied probability and stochastic modeling
- Bridges theory with simulation
- Highlights convergence and stability properties of Markov systems
