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


class CausalBandit:
    """
    Causal Bandit Class

    A causal bandit is a bandit where variables relations are represented on a causal graph/SCM.
    In this general case, variables are named X_i.
    """

    def __init__(
        self,
        structural_causal_model, 
        number_of_episode = 40,
    ):
        """
        Instantiate Causal Bandit Class

        Parameters
        ----------
        structural_causal_model: StructuralCausalModel instance
            the Structurral Causal Model of the Causal Bandit. 

        """
        
        self.scm = structural_causal_model
        self.payout_history: List[int] = []
        self.counter = 0
        self.episode = number_of_episode

    def get_sample(self, action):
        """
        Return the payout of a single pull of causal bandit i's arm. 

        Parameters
        ----------
        i: int
            Index of causal bandit to pull.

        Returns
        ----------
        int or None
        """
        arm, action_value = action

        # sample the scm with the manipulated variables "arm" set to "action_value"
        output = self.scm.get_sample(set_values={arm : action_value})

        # save the reward 
        self.payout_history.append(output)

        return output

    def step(self, action: Tuple[str, int]):
        """ Excecute action on env and returns reward, info, observation and done. 

        Parameters
        ----------
        action : tuple[variable, float]
            Action to execute.

        Returns
        ----------
        reward: float
        info: str
        observation: dict[variable, float]
        is_done: boolean
        """

        observation = self.get_sample(action)
        reward = observation["Y"]
        is_done = (self.counter >= self.episode)
        info = "Round n°{} of {}".format(self.counter, self.episode)

        self.counter += 1
        
        return (observation, reward, is_done, info)