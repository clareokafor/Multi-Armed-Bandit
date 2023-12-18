# -*- coding: utf-8 -*-
# OGOCHUKWU JANE OKAFOR

# MULTI-ARMED BANDIT

import numpy as np
import matplotlib.pyplot as plt

# intitialize number of k bandits 
k = 10

# Define the action values for each bandit arm as a random normal distribution with mean of 0 and variance of 1.
Q_star = np.random.normal(2, 4, k)

# set up list of epsilon values to test
epsilons = (0, 0.01, 0.1)

# number of time steps 
time_steps = 4000

# Define an array to store the average reward obtained for each epsilon value
average_shape = (len(epsilons), time_steps)
average_rewards = np.zeros(average_shape)

# for each epsilon values ,the multi-armed bandit is implemented
for index, epsilon in enumerate(epsilons):
    
    # initialize estimates
    Q = np.zeros(k)

    # intialize number of times an armed has been pulled to zero
    N = np.zeros(k)

    # initialize array to store rewards
    rewards = np.zeros(time_steps)

    # Start epsilon greedy procedure
    for time in range(time_steps):
        # Select arm to play
        if np.random.random() > epsilon:
            # Exploitation by choosing arm with highest estimate
            arm = np.argmax(Q)
        else:
            # Exploration
            arm = np.random.randint(k)

        # Obtain reward of the chosen arm from action distribution.
        reward = np.random.normal(Q_star[arm], 1)

        # Apply update rule on estimate of action value for the selected bandit
        N[arm] += 1
        Q[arm] += (reward - Q[arm])/N[arm]

        # Store collected rewards
        rewards[time] = reward

    # Compute the average reward obtained over all time steps and store it in the averageg_rewards array
    average_rewards[index] = np.cumsum(rewards)/np.arange(1, time_steps + 1)

# Plotting average reward collected over time step
for index, epsilon in enumerate(epsilons):
    plt.plot(average_rewards[index], label="epsilon = %.2f"%epsilon)
    plt.ylabel("Average reward collected")
    plt.xlabel("Time step")
    plt.legend()
