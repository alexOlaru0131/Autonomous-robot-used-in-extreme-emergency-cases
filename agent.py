# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 06:15:58 2025

@author: alexo
"""

from collections import defaultdict
import gymnasium as gym
import numpy as np

class Agent:
    def __init__(self,
                 env: gym.Env,
                 learning_rate: float,
                 initial_epsilon: float,
                 epsilon_decay: float,
                 final_epsilon: float,
                 discount_factor: float):
        self.env = env
        self.q_values = defaultdict(lambda: np.zeros(env.action_space.n))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = initial_epsilon
        self.epsilon_decay = epsilon_decay
        self.final_epsilon = final_epsilon
        self.training_error = []
        
    def get_action(self, obs: tuple[int, int, bool]) -> int:
        if np.random().random() < self.epsilon:
            return self.env.action_space.sample()
        else:
            return int(np.argmax(self.q_values[obs]))
        
    def update(self,
               obs: tuple[int, int, bool],
               action: int,
               reward: float,
               terminated: bool,
               next_obs: tuple[int, int, bool]):
        future_q_value = (not terminated) * np.max(self.q_values[next_obs])
        target = reward + self.discount_factor * future_q_value
        temporal_differece = target - self.q_values[obs][action]
        self.q_values[obs][action] = ( self.q_values[obs][action] + self.learning_rate * temporal_differece )
        self.training_error.append(temporal_differece)
        
    def decay_epsilon(self):
        self.epsilon = max(self.final_epsilon, self.epsilon - self.epsilon_decay)
        
        
        
        
        
        
        
        
        
        
        
        
        
        