# -*- coding: utf-8 -*-

"""

The classes of this file simulates decision-making environments called causal bandits. 

@author: elichou
"""
from typing import *
import networkx as nx
from typing import *
import scipy.stats as st
import random
import numpy as np
import matplotlib.pyplot as plt

variable = str
structural_function = Callable[[tuple[variable, Union[int,None]]], int]

class StructuralCausalModel: 
    """
    Structural Causal Model for Causal Bandit implementation.
    """

    def __init__(
        self,
        variables: list[variable], 
        structural_equations: 
            dict[variable, tuple[structural_function, dict[variable, Union[int,None]]]], 
    ):
        """
        Instantiate StructuralCausalModel class.

        Parameters
        ----------

        variables: list[variable:str]
            List containing the name of the variables. 

        structural_equations: dict[variable: (func, list[variable:str])]
            A dictionary containing the structural relations between variables
            and their values. 
        """
        self.variables = variables
        self.structural_equations = structural_equations
        self.causal_graph = self.build_causal_graph(variables, structural_equations)

    def build_causal_graph(
        self, 
        variables: list[variable],
        structural_equations: 
            dict[variable, tuple[structural_function, dict[variable, Union[int,None]]]]
        ) -> nx.DiGraph: 

        """
        Build a causal graph from variables list and structural equations. 

        Parameters
        ----------

        variables: list[variable]

        structural_equations: dict[variable, eqution]

        Returns
        ----------

        a DiGraph

        """
        output_graph = nx.DiGraph()
        nodes = variables
        edges = []
        
        for variable, equation in structural_equations.items(): 
            children_node = variable
            (function, vars) = equation
            for var, value in vars.items():
                parent_node = var
                edges.append((parent_node, children_node))

        output_graph.add_nodes_from(nodes)
        output_graph.add_edges_from(edges)

        return output_graph

    def sample(self, set_values: Optional[Union[dict[variable, int],None]] = None) -> int:
        """
        Sample from SCM (could be manipulated through set_values).

        Parameters
        ----------

        set_values: dict[variable, int]
            The values fixed by intervention on variables.

        Returns
        ----------

        sample: int

        """
        output_assignments = {}
    
        if set_values is not None:
            for variable, value in set_values.items(): # assign values to manipulated variables
                output_assignments[variable] = value

            for node in self.causal_graph.nodes: # assign values to manipulated parent variables
                structural_function, parents = self.structural_equations[node]
                for parent in parents.keys():
                    if parent in set_values.keys():
                        parents[parent] = set_values[parent]
        
            for node in nx.topological_sort(self.causal_graph): # assign values to remaining variables
                if node in set_values.keys():
                    pass
                else:
                    structural_function, parents = self.structural_equations[node]
                    output_assignments[node] = structural_function(parents)
        else:
            for node in nx.topological_sort(self.causal_graph): # assign values to all variables
                structural_function, parents = self.structural_equations[node]
                output_assignments[node] = structural_function(parents) 

        return output_assignments
    
