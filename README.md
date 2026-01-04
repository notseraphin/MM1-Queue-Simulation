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
│   ├── queue.py        # Event-driven M/M/1 simulator
│   ├── analysis.py     # Theoretical + empirical analysis
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

**Technologies Used**

- Python
- NumPy
- Matplotlib
- Jupyter Notebooks

**Key Takeaways**

- Demonstrates applied probability and stochastic modeling
- Bridges theory with simulation
- Highlights convergence and stability properties of Markov systems
