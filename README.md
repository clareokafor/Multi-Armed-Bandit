# 🎰 Multi-Armed Bandit Simulation with ε-Greedy Strategy

This project implements a simulation of the **Multi-Armed Bandit** problem using the **ε-greedy algorithm**, exploring the trade-off between **exploration and exploitation** across different epsilon values.

## 📌 Overview

In reinforcement learning, the Multi-Armed Bandit problem is a fundamental scenario used to illustrate how an agent can learn optimal actions through interaction with an environment. This project models:

* 10 bandit arms (slot machines)
* Reward distributions drawn from a normal distribution (mean = 2, variance = 4)
* Time horizon of 4000 steps
* ε-greedy strategy evaluated for `ε = 0`, `0.01`, and `0.1`

## 🧠 Algorithm Details

The **ε-greedy algorithm** chooses a random action (exploration) with probability ε and the best-known action (exploitation) with probability 1−ε. This helps in striking a balance between trying new actions and sticking to the best-known ones.

At each time step:

* With probability ε, choose a random arm.
* Otherwise, select the arm with the highest estimated value.
* Receive a reward based on the true distribution of the selected arm.
* Update the estimated value of the arm using incremental averaging.

## 📊 Results

The script produces a plot of average reward over time for each ε value:

* `ε = 0` (pure exploitation)
* `ε = 0.01` (low exploration)
* `ε = 0.1` (moderate exploration)

These results clearly illustrate how a small amount of exploration can significantly improve long-term performance.

![ε-greedy plot](f)

## 🚀 Getting Started

### Requirements

* Python 3.x
* NumPy
* Matplotlib


## 🧪 Insights

The ε-greedy algorithm consistently outperforms pure greedy approaches by efficiently balancing information gathering with reward maximization. Its adaptability and simplicity make it a powerful tool in online decision-making scenarios.
