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


class StructuralCausalModel: 
    """
    Structural Causal Model for Causal Bandit implementation.
    """

    def __init__(
        self,
        variables: List[str], 
        structural_equations: Dict[str, Tuple[Callable[[Tuple[int, Union[int, None]]], int], Dict[str, Union[int, None]]]]
             
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
        self.variables = variables # list of variables
        self.values = { var: None for var in variables } # list of values taken by each variable
        self.structural_equations = structural_equations # functions for each variable
        self.causal_graph = self.build_causal_graph(variables, structural_equations) # a causal graph of the SCM

    def build_causal_graph(
        self, 
        variables: List[str],
        structural_equations: Dict[str, Tuple[Callable[[Tuple[int, Union[int, None]]], int], Dict[str, Union[int, None]]]]
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

    def graph(self):
        """ Draw the internal causal graph
        """
        nx.draw(self.causal_graph)

    def get_sample(self, set_values: Optional[Union[Dict[str, int],None]] = None) -> dict[str, Union[int, None]]:
        """
        Sample from SCM (could be manipulated through set_values).

        Parameters
        ----------
        set_values: dict[variable, int]
            The values fixed by intervention on variables.

        Returns
        ----------
        output_assignements : dict[variable, int] 

        """


        output_assignments = {var : None for var in self.variables}

        if set_values is not None: 
            
            # Assign values to manipulated variables
            for variable, value in set_values.items():
                output_assignments[variable] = value
                self.values[variable] = value
            
            # Assign values inside the structural_equations for variables which parents are manipulated variables
            for node in self.causal_graph.nodes:
                structural_function, parents = self.structural_equations[node]
                for parent in parents.keys():
                    if parent in set_values.keys():
                        parents[parent] = set_values[parent]

            # Assign values to remaining variables for output
            for node in nx.topological_sort(self.causal_graph):
                if node in set_values.keys():
                    pass
                else:
                    structural_function, parents = self.structural_equations[node]
                    output_assignments[node] = structural_function(parents)  
                    # when a value is assigned, make sure that it is also assigned in the structural_equations 
                    for node2 in self.causal_graph.nodes:
                        structural_function, parents = self.structural_equations[node2]
                        if node in parents.keys():
                            parents[node] = output_assignments[node]

        else:
            for node in nx.topological_sort(self.causal_graph):
                    structural_function, parents = self.structural_equations[node]
                    output_assignments[node] = structural_function(parents)  
                    # when a value is assigned, make sure that it is also assigned in the structural_equations 
                    for node2 in self.causal_graph.nodes:
                        structural_function, parents = self.structural_equations[node2]
                        if node in parents.keys():
                            parents[node] = output_assignments[node]


        return output_assignments  

        """
        output_assignments = {}
    
        if set_values is not None: 
            
            # Assign values to manipulated variables
            for variable, value in set_values.items(): 
                output_assignments[variable] = value
                self.values[variable] = value
                
            # Assign values to manipulated parent variables
            for node in self.causal_graph.nodes: 
                structural_function, parents = self.structural_equations[node]
                for parent in parents.keys():
                    if parent in set_values.keys():
                        parents[parent] = set_values[parent]
                        self.values[parent] = set_values[parent]
        
            # Assign values to remaining variables 
            for node in nx.topological_sort(self.causal_graph): 
                if node in set_values.keys():
                    continue
                structural_function, parents = self.structural_equations[node]
                output_assignments[node] = structural_function(parents)
   
        else:
            # Assign values to all variables
            for node in nx.topological_sort(self.causal_graph): 
                structural_function, parents = self.structural_equations[node]
                output_assignments[node] = structural_function(parents) 

        # Assign values inside the equations
        for key, value in self.structural_equations.items(): 
            function, parent_di = value
            for key2, value2 in parent_di.items():
                parent_di[key2] = self.values[key2]
        
        return output_assignments
        """