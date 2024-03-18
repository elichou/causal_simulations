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


class OCTSAgent_with_graph(Agent):
    """
    OCTS agent without causal graph knowledge
    """

    def __init__(self, actions: list[variable, float], env):
        super().__init__(actions)
        self.K = len(self.actions)
        self.n_part = 4
        self.beta = np.ones([self.n_part, self.K], dtype=int)
        self.env = env

    def choose_action(self, observation):

        # update
        list_observation = [(key, value) for key, value in observation.items()]
        z = sum([2**i * list_observation[i][1] for i in range(len(list_observation)-1)])
        

        # sample        
        success_chance = np.zeros(self.K)

        for a in range(self.K):
            partition_prob = np.array([[st.bernoulli.rvs(self.env.params[4]), st.bernoulli.rvs(1-self.env.params[4])]]).reshape(-1, 1)
            sample_prob = np.random.beta(self.beta[:,0], self.beta[:, 1]).reshape(-1,1)
            success_chance[a] = sum(np.matmul(sample_prob, partition_prob.T))[0]
            print("success_chance:{}".format(success_chance))

        # select action
        action_index = np.argmax(success_chance)

        return self.actions[action_index]



    def __name__(self):
        return 'OCTSAgentWithGraph'