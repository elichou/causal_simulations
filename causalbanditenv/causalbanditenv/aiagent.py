import scipy
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

class AIAgent(Agent):
    """ 
    """
    def __init__(self, actions: list[variable, float]):
        super().__init__(actions)
        self.K = len(actions)
        self.beta_params = [(1, 1) for k in range(self.K)]
        self.precision = 1.0
        
    def choose_action(self, observation, previous_action) : #, tmp = []):

        # update beta params
        var, value = previous_action
        index = self.actions.index((var, value)) # corriger erreur ici
        alpha_x, beta_x = self.beta_params[index]
        self.beta_params[index] = (alpha_x + observation["Y"], beta_x + 1 - observation["Y"])

        # compute approximate free energy
        est_eff = []
        tmp2 = []
        for k in range(self.K):
            alpha, beta = self.beta_params[k]
            nu = alpha + beta
            mu = alpha/nu
            est_eff.append(2*self.precision*mu + 1/(2*nu))
            tmp2.append(2*self.precision*mu + 1/(2*nu))

        #tmp.append(scipy.special.softmax(tmp2)) 
        #print("g:{}".format(est_eff))
        # select action
        action_index = np.argmax(est_eff)

        return self.actions[action_index] #, tmp



    def __name__(self):
        return 'AIAgent'

