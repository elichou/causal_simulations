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


def triangle(x):
    output = None
    if x < 1/2:
        output = 2*x
    else:
        output = -2*x + 2
    
    return output


class AIBanditAgent(Agent):

    def __init__(self, actions: list[variable, float], param: float, precision:float = 0.1):
        super().__init__(actions)
        self.K = len(actions)
        self.beta_params = [(1, 1) for k in range(self.K)]  
        self.precision = precision
        self.rho = triangle(param)
    
    def choose_action(self, observation):

        # update beta params
        index = self.actions.index(("X", observation["X"]))
        alpha_x, beta_x = self.beta_params[index]
        self.beta_params[index] = (alpha_x + observation["Y"], beta_x + 1 - observation["Y"])
        
        # compute approximate free energy
        g = []
        
        for k in range(self.K):
            alpha, beta = self.beta_params[k]
            nu_1 = alpha + beta
            mu_1 = alpha/nu_1
            mu = mu_1 + self.rho*(0.5 - mu_1)

            g_a = -2*self.precision*(1-self.rho)*mu_1 + mu*np.log(mu) + (1-mu)*np.log(1 - mu) - \
                 (1 - self.rho)*(mu_1*special.digamma(alpha) + 1 - mu_1*special.digamma(beta)) + \
                    (1 - self.rho)*(special.digamma(nu_1)-1/nu_1) + 1
            g.append(g_a)
        
        # select action
        action_index = np.argmax(g)
        
        return self.actions[action_index]