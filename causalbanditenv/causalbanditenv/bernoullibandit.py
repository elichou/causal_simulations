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

class BernoulliBandit(CausalBandit):
    """ Bernoulli Bandit with two choices: (X=0) or (X=1).
    """
    
    def __init__(self, params=[0.3,0.6,0.6,0.8], episode=40):
        """ Instantiate a Bernoulli Causal Bandit.

        Parameters
        ----------

        params: list[float]
            List of Bernoulli parameters.
            X |  P(Y|X)
            --------------------
            0 |  params[0]
            1 |  params[1]

        """
        
        self.counter = 0
        self.episode = episode
        self.params: Optional[list[float]] = params
        self.variables = ["X", "Y"] 
        self.best_hist_payouts = []
        self.regrets = []

        def best_arm(params):
            """ Identify the best arm for bernoulli statitc causal bandit. 
            
            """
            index = np.argmax(params)
            output = np.mod(index, 2)
            return output

        self.best_arm = best_arm(params)
 
        def f_X(arg: dict[tuple[variable, int]]) -> int:
            """ function for X
            """
            output = st.bernoulli.rvs(0.5)
            return output
        
        def f_Y(arg: dict[tuple[variable, int]]) -> int:
            """ function for Y
            """
            output = 0
            x_value = arg["X"]
            if x_value == 0:
                output = st.bernoulli.rvs(self.params[0])
            else:
                output = st.bernoulli.rvs(self.params[1])
            return output

        structural_equations = {
            "X" : (f_X, {}),
            "Y" : (f_Y, { "X" : None}),
        }

        scm = StructuralCausalModel(self.variables, structural_equations)
        super().__init__(scm)

    def pull(self, i: float): 
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
        output = self.scm.get_sample(set_values={"X" : i})
        #best_output = self.scm.sample(set_values = {"X" : self.best_arm})
        best_output = 1
        self.regrets.append(best_output - output["Y"])
        self.payout_history.append(output)
        return output  

    def step(self, action: tuple[variable, float]):
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
        done: boolean
        """
        var, value = action 

        observation = self.pull(value)
        reward = observation["Y"]
        done = (self.counter >= self.episode)
        info = "Round n°{}".format(self.counter)
        self.counter += 1
        return (observation, reward, done, info)

    def reset(self):
        self.counter = 0
        observation = {}
        for var in self.variables:
            observation[var] = 0
        self.regrets = []
        return observation

    def __name__(self):
        return 'BernoulliBandit'