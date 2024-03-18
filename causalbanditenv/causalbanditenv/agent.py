from .causalbandit import CausalBandit
from .structuralcausalmodel import StructuralCausalModel
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

class Agent:
    """
    Generic class for agent model implementation.
    """

    def __init__(self, actions: list[variable, float]):
        """
        Instantiate a model for decision making on causal bandit envs.

        Parameters
        ----------
        actions : list[variable, float]
            list of possible actions. 
        
        """
        self.actions = actions

    
    def choose_action(self, observation, previsou_action=None):
        """ default is random sample. 
        """
        action = random.choices(self.actions)
        return action[0]


    def __name__(self):
        return 'RandomAgent'