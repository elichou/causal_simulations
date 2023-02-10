from causal_simulations import __version__
import causal_simulations
import networkx as nx
import typing
import scipy.stats as st
import random
import numpy as np
import matplotlib.pyplot as plt
import pymdp
from tqdm import tqdm

def test_version():
    assert __version__ == '0.1.0'

# test
def test_build_causal_graph():
    print("Test_build_causal_graph...")
    def f_U(arg: dict[tuple[variable, int]]) -> int:
        return st.norm.rvs(1)

    def f_Z(arg: dict[tuple[variable, int]]) -> int:
        output = 0
        for var, value in arg.items():
            if value:
                output += 0.1*value
            else:
                pass
        return output

    def f_X(arg: dict[tuple[variable, int]]) -> int:
        output = 0
        for var, value in arg.items():
            if value:
                output += 0.1*value
            else:
                pass
        return output

    def f_Y(arg: dict[tuple[variable, int]]) -> int:
        output = 0
        for var, value in arg.items():
            if value:
                output += 0.1*value
            else:
                pass
        return output

    variables = ["X", "Y", "Z", "U_X", "U_Y", "U_Z"]
    structural_equations = {
        "X": (f_X, {"U_X": None}),
        "Y": (f_Y, {"U_Y": 0, "X": 1}),
        "Z": (f_Z, {"U_Z": None}),
        "U_X": (f_U, {}),
        "U_Z": (f_U,{} ),
        "U_Y": (f_U, {})}

    scm = StructuralCausalModel(variables, structural_equations)
    assert(scm.causal_graph.edges)
    assert(scm.causal_graph.nodes)
    assert(nx.is_directed_acyclic_graph(scm.causal_graph))
    print("SUCCESS")

def test_sample_scm():
    print("Test_sample_scm...")

    def f_U(arg: dict[tuple[variable, int]]) -> int:
        return st.norm.rvs(1)

    def f_Z(arg: dict[tuple[variable, int]]) -> int:
        output = 0
        for var, value in arg.items():
            if value:
                output += 0.1*value
            else:
                pass
        return output

    def f_X(arg: dict[tuple[variable, int]]) -> int:
        output = 0
        for var, value in arg.items():
            if value:
                output += 0.1*value
            else:
                pass
        return output

    def f_Y(arg: dict[tuple[variable, int]]) -> int:
        output = 0
        for var, value in arg.items():
            if value:
                output += 0.1*value
            else:
                pass
        return output
    variables = ["X", "Y", "Z", "U_X", "U_Y", "U_Z"]
    structural_equations = {
        "X": (f_X, {"U_X": None}),
        "Y": (f_Y, {"U_Y": 0, "X": 1}),
        "Z": (f_Z, {"U_Z": None}),
        "U_X": (f_U, {}),
        "U_Z": (f_U,{} ),
        "U_Y": (f_U, {})}

    scm = causal_simulations.StructuralCausalModel(variables, structural_equations)
    assert(scm.sample(set_values={"X":1}))
    assert(scm.sample())
    print("SUCCESS")

test_build_causal_graph()
test_sample_scm()

# test
def test_causal_bandit():

    """ Test de causal bandit
    """
    print("Test_causal_bandit...")
    def f_U(arg: dict[tuple[variable, int]]) -> int:
        return st.norm.rvs(1)

    def f_Z(arg: dict[tuple[variable, int]]) -> int:
        output = 0
        for var, value in arg.items():
            if value:
                output += 0.1*value
            else:
                pass
        return output

    def f_X(arg: dict[tuple[variable, int]]) -> int:
        output = 0
        for var, value in arg.items():
            if value:
                output += 0.1*value
            else:
                pass
        return output

    def f_Y(arg: dict[tuple[variable, int]]) -> int:
        output = 0
        for var, value in arg.items():
            if value:
                output += 0.1*value
            else:
                pass
        return output

    variables = ["X", "Y", "Z", "U_X", "U_Y", "U_Z"]
    structural_equations = {
        "X": (f_X, {"U_X": None}),
        "Y": (f_Y, {"U_Y": 0, "X": 1}),
        "Z": (f_Z, {"U_Z": None}),
        "U_X": (f_U, {}),
        "U_Z": (f_U,{} ),
        "U_Y": (f_U, {})}
    scm = StructuralCausalModel(variables=variables, structural_equations=structural_equations)

    causal_bandit = CausalBandit(structural_causal_model=scm)

    assert(causal_bandit.pull(1))
 
    print("SUCCESS")

test_causal_bandit()

def test_bernoulli_bandit():
    """ test bernoulli classic bandit
    """
    print("Test Bernoulli classic Bandit")
    bernoulli = BernoulliBandit()
    print("SUCCESS")

test_bernoulli_bandit()

# test
def test_bernoulli_causal_bandit():
    """ test bernoulli causal bandit
    """
    print("Test Bernoulli Causal Bandit...")
    bernoulli = BernoulliCausalBandit([0.1, 0.9, 0.2, 0.8])
    print(bernoulli.regrets)
    #print(bernoulli.pull(1))
    #print(bernoulli.scm.structural_equations)
    #print(bernoulli.scm.hist_payouts)
    print("SUCCESS")
    
test_bernoulli_causal_bandit()

# test
def test_agent():
    """ test agent class
    """
    print("test_agent")

    actions = [("X",0),("X",1)]
    agent = Agent(actions)
    assert(agent.choose_action())
    
    print("SUCCESS")

test_agent()

def test_TSAgent():
    print("test TS Agent")
    ACTIONS = [("X",0),("X",1)]

    agent = TSAgent(ACTIONS)

    print("SUCCESS")

test_TSAgent()

def test_OCTSAgent():
    print("test OCTS agent")
    ACTIONS = [("X",0),("X",1)]
    agent = OCTSAgent(ACTIONS)
    print("SUCCESS")

test_OCTSAgent()

# test 
def test_AIAgent():
    print("test AI Agent")
    ACTIONS = [("X",0),("X",1)]
    agent = AIAgent(ACTIONS)
    print("SUCCESS")

test_AIAgent()