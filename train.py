# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 06:01:18 2025

@author: alexo
"""

import gymnasium as gym
from agent import Agent

env = []
N = []

learning_rate = 0.01
n_episodes = 100
start_epsilon = 1.0 
epsilon_decay = start_epsilon / (n_episodes / 2)
final_epsilon = 0.1 
discount_factor = 0.95

#agent = Agent(env = env,
#              learning_rate,
#              initial_epsilon,
#              epsilon_decay,
#              final_epsilon,
#              dicount_factor)

episode_over = False
total_reward = 0

for _ in range(N):
    observation, info = env.reset()
    while not episode_over:
        action = []
#        action = agent.get_action(obs)
        
        new_observation, reward, terminated, truncated, info = env.step(action)
#        agent.update(observation, action, reward, terminated, new_observation)
        
        total_reward += reward
        episode_over = terminated or truncated
        observation = new_observation
    
#    agent.decay_epsilon()
        
env.close()