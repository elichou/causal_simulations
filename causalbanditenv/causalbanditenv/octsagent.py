from .causalbandit import CausalBandit
from .structuralcausalmodel import StructuralCausalModel
from .agent import Agent
import networkx as nx
from typing import Callable, Union, Tuple, Dict, List, Optional
import scipy.stats as st
import random
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import scipy.special as special
import warnings

variable : Union[str, None] = None
structural_function : Callable[[Tuple[int, Union[int, None]]], int] 
structural_equations: Dict[str, Tuple[Callable[[Tuple[int, Union[int, None]]], int], Dict[str, Union[int, None]]]] = {}


class OCTSAgent(Agent):
    """
    OCTS agent without causal graph knowledge
    """

    def __init__(self, actions: list[variable, float]):
        super().__init__(actions)
        self.K = len(self.actions)
        self.n_part = 4
        self.dirc = np.ones([self.n_part, self.K], dtype=int)
        self.beta = np.ones([self.n_part, 2], dtype=int)

    def choose_action(self, observation, previous_action=None):
        """ Select action based on OCTS algorithm
            Note that X is always manipulated here
            so this does not work for an observational setting.
        """

        # update
        list_observation = [(key, value) for key, value in observation.items()]
        z = sum([2**i * list_observation[i][1] for i in range(len(list_observation)-1)])
        self.dirc[z, int(observation["X"])] += 1
        self.beta[z, 1 - int(observation["Y"])] += 1

        # sample        
        success_chance = np.zeros(self.K)

        for a in range(self.K):
            partition_prob = np.random.dirichlet(self.dirc[:,a]).reshape(-1,1)
            sample_prob = np.random.beta(self.beta[:, 0], self.beta[:, 1]).reshape(-1,1)
            success_chance[a] = sum(np.matmul(sample_prob.T, partition_prob))[0]
            
        # select action
        action_index = np.argmax(success_chance)
        
        return self.actions[action_index]


    def __name__(self):
        return 'OCTSAgent'