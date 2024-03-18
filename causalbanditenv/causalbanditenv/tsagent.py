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


class TSAgent(Agent):
    """ Thompson Sampling
    """
    def __init__(self, actions: list[variable, float]):
        super().__init__(actions)
        self.K = len(actions)
        self.beta_params = [(1, 1) for k in range(self.K)]
        
    def choose_action(self, observation, previous_action=None):

        # update beta params
        index = self.actions.index(("X", observation["X"]))
        alpha, beta = self.beta_params[index]
        self.beta_params[index] = (alpha + observation["Y"], beta + 1 - observation["Y"])

        # sample model
        theta_est = []
        for k in range(self.K):
            theta_est.append(st.beta.rvs(self.beta_params[k][0], self.beta_params[k][1]))

        # select action
        action_index = np.argmax(theta_est)
        return self.actions[action_index]

    def __name__(self):
        return 'TSAgent'