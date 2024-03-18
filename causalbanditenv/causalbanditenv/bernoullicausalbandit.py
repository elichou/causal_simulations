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


class BernoulliCausalBandit(CausalBandit):
    """ Bernoulli Bandit with two choices: (X=0) or (X=1).   
    """
    
    def __init__(self, params, number_of_episode=40):

        """ Instantiate a Bernoulli Causal Bandit.

        Parameters
        ----------
        params: list[float]
            List of Bernoulli parameters.

            Z |  P(Y = 1 | X = 1, Z)    |   P(Y = 1 | X = 0, Z)
            --|-------------------------|----------------------
            0 |  params[0]              |   params[1]
            1 |  params[2]              |   params[3]



            Z ~ P(Z) = Bern(params[4]) 

        
        """

        self.counter = 0
        self.episode = number_of_episode
        self.params: Optional[List[float]] = params # list of Bernoulli parameters
        self.variables = ["X", "Y", "Z"] 
        self.history_best_payout = []
        self.regrets = []


        def best_arm(params):
            """ Identify the best arm for bernoulli static causal bandit. 
                pair ou impair et pas supérieur ou inférieur
            """
            index = np.argmax(params)
            output = np.mod(index, 2)

            return output

        self.best_arm = best_arm(params)
 
        def f_X(arg: dict[tuple[variable, int]]) -> int:
            """ function for X
                not used in practive because X is always manipulated
            """
            if arg["Z"] == 0:
                return st.bernoulli.rvs(self.params[5])
            else:
                return st.bernoulli.rvs(self.params[6])

        def f_Y(arg: dict[tuple[variable, int]]) -> int:
            """ function for Y
            """
            dict_values = {(0, 0): 1, (0, 1): 3, (1, 0): 0, (1, 1) : 2, (0, None): 1, (1, None): 3}
            
            return st.bernoulli.rvs(self.params[dict_values[(arg["X"], arg["Z"])]])

        def f_Z(arg: dict[tuple[variable, int]]) -> int:
            """ function for Z
            """
            
            return st.bernoulli.rvs(self.params[4])

        structural_equations = {
            "Z" : (f_Z, {}),
            "X" : (f_X, { "Z" : None}),
            "Y" : (f_Y, { "X" : None, "Z" : None}),
        }

        scm = StructuralCausalModel(self.variables, structural_equations)

        super().__init__(scm)

    def get_sample(self, action: float): 
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
        if action != {}:
            arm, action_value = action
            output = self.scm.get_sample(set_values={arm : action_value})
        else:
            output = self.scm.get_sample({})




        self.regrets.append(1 - output["Y"])
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


        observation = self.get_sample(action)
        reward = observation["Y"]
        is_done = (self.counter >= self.episode)
        info = "Round n°{}".format(self.counter)

        self.counter += 1
        
        return (observation, reward, is_done, info)

    def reset(self):
        """ Reset the observation and the counter of the environment
        """
        self.counter = 0
        self.regrets = []
        
        return {var : 0 for var in self.variables}

    def __name__(self):
        return 'BernoulliCausalBandit'