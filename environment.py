# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 06:12:46 2025

@author: alexo
"""

import gymnasium as gym
from gymnasium import spaces, gymspaces
from communication import I2C_COMMUNICATION
from typing import Optional

class Environment(gym.Env):
    def __init__(self, sizeX, sizeY, I2C_COMMUNICATION):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.I2C_COMMUNICATION = I2C_COMMUNICATION
        
        self.observation_space = spaces.Dict({
            "turning_points": gymspaces.Sequence(spaces.Box(0, 2, shape=(2,), dtype = int)),
            "distances": gymspaces.Sequence(spaces.Box(0, sizeX, sizeY, shape=(2,), dtype = int)),
            })
        self.action_space = gym.spaces.Discrete(4)
        self._action_to_direction = {
            0: lambda: I2C_COMMUNICATION.generateTelemetry(0x01),
            1: lambda: I2C_COMMUNICATION.generateTelemetry(0x02),
            2: lambda: I2C_COMMUNICATION.generateTelemetry(0x03),
            3: lambda: I2C_COMMUNICATION.generateTelemetry(0x04),
            }
        
    def _get_obs(self) -> None:
        return
    
    def _get_info(self) -> None:
        return
    
    def reset(self, seed: Optional[int] = None, options: Optional[dict] = None):
        return
    
    def step(self, action):
        return