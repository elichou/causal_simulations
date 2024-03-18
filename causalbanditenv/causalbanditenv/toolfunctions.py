import scipy
from .causalbandit import CausalBandit
from .bernoullicausalbandit import BernoulliCausalBandit
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


def f(name):
    if name == "AIAgent":
        print('ok')
    else:
        print("notok")

f("AIAgent")

def compute_probs(rewards, actions):

    with warnings.catch_warnings():

        warnings.simplefilter("ignore")

         

        # compute probability to win when the agent's play
        win_play = [((action[1] and reward)) for (action, reward) in zip(actions, rewards)]
        num_win_play = [np.sum(win_play[:i]) for i in range(len(win_play))]
        num_play = [np.sum([action[1] for action in actions[:i]]) for i in range(len(actions))]
        p_win_play = [win_play_t/play_total_t for (win_play_t, play_total_t) in zip(num_win_play, num_play)]

        # compute the probability to win when the agent doesn't play
        win_no_play = [int(not(action[1]) and reward) for (action, reward) in zip(actions, rewards)]
        num_win_no_play = [np.sum(win_no_play[:i]) for i in range(len(win_no_play))]
        num_no_play = [np.sum([int(not(action[1])) for action in actions[:i]]) for i in range(len(actions))]
        p_win_no_play = [win_no_play_t/no_play_t for (win_no_play_t, no_play_t) in zip(num_win_no_play, num_no_play)]

        # compute probability of play
        p_win_play = [(0.5 if np.isnan(p) else p) for p in p_win_play]
        p_win_no_play = [(0.5 if np.isnan(p) else p) for p in p_win_no_play]

        p_play = [num_play/i for (i, num_play) in enumerate(num_play)]

        return p_win_play, p_win_no_play, p_play

def plot_prob(agent_name: str, env_name: str, actions, switch: float=0.0, reset_agent: bool=True, change: bool = False):

    
    index = ["0.6", "0.4", "0.0", "-0.4"]
    fig, axs = plt.subplots(1, 4, figsize=(20,5))
    fig.suptitle(agent_name)

    with warnings.catch_warnings():

        warnings.simplefilter("ignore")   

        for k in range(4):
            list_params = [[0.8, 0.2, 0.7, 0.3, switch],
                        [0.7, 0.3, 0.7, 0.3, switch],
                        [0.5, 0.5, 0.5, 0.5, switch],
                        [0.3, 0.7, 0.3, 0.7, switch]
                        ]
            
            if str(env_name).find('BernoulliCausalBandit') > 0:
                list_params = [[0.8, 0.2, 0.7, 0.3, 0.5, 0.5, switch],
                        [0.7, 0.3, 0.7, 0.3, 0.5, 0.5, switch],
                        [0.5, 0.5, 0.5, 0.5,0.5, 0.5, switch],
                        [0.3, 0.7, 0.3, 0.7,0.5, 0.5, switch]
                        ]
                        
            PARAMS = list_params[k]
            env = env_name(PARAMS)
            observation = {'X': 0, 'Y': 0, 'Z': 0}
        
            if not(reset_agent):
                agent = agent_name(actions)

            list_pwp = []
            list_pwnp = []
            list_play = []

            for i in tqdm(range(100)):

                hist_observations = []
                hist_randag_rewards = []
                hist_randag_actions = []
                observation = env.reset()

                if reset_agent:
                    agent = agent_name(actions)

                previous_action = agent.actions[np.random.randint(2)]

                for t in range(40):
                    if ((t == 20) and change):
                        observation = env.reset()


                    if (str(agent).find("AIAgent") > 0 ):
                        action = agent.choose_action(observation, previous_action)
                        previous_action = action
                    else:
                        action = agent.choose_action(observation)
                        
                    observation, reward, done, info = env.step(action)
                    hist_randag_rewards.append(reward)
                    hist_randag_actions.append(action)
                    
                    #if done:
                    #     print("End of this episode.")
                    #    break
                    

                randag_pwp, randag_pwnp, p_play = compute_probs(hist_randag_rewards, hist_randag_actions)
                list_pwp.append(randag_pwp)
                list_pwnp.append(randag_pwnp)
                list_play.append(p_play)


            list_pwp = np.asarray(list_pwp)
            _, m = np.shape(list_pwp)
            
            pwp_means = np.asarray(([np.nanmean(list_pwp[:,j]) for j in range(m)]))
            pwp_stds = np.asarray(([np.nanstd(list_pwp[:,j]) for j in range(m)]))

            x = np.arange(m) 
            
            axs[0].plot(x, pwp_means, label="P(win|play)={}".format(PARAMS[0]))
            axs[0].fill_between(x, pwp_means-pwp_stds, pwp_means+pwp_stds, alpha = 0.2, )
            #axs[0].set_title('P(win|play)')
            axs[0].set_xlabel('Time Horizon')  # Replace 'X-axis Label' with your actual x-axis label
            axs[0].set_ylabel('P(win|play)') 
            axs[0].legend()

            list_pwnp = np.asarray(list_pwnp)
            _, m = np.shape(list_pwnp)
            
            pwnp_means = np.asarray(([np.nanmean(list_pwnp[:,j]) for j in range(m)]))
            pwnp_stds = np.asarray(([np.nanstd(list_pwnp[:,j]) for j in range(m)]))

            pwnp_means = np.nan_to_num(pwnp_means)
            pwnp_stds = np.nan_to_num(pwnp_stds)
            
            x = np.arange(m)

            axs[1].plot(x, pwnp_means, label="P(win|not play)={}".format(PARAMS[1]))
            axs[1].fill_between(x, pwnp_means-pwnp_stds, pwnp_means+pwnp_stds, alpha = 0.2)
            #axs[1].set_title('P(win|not play)')
            axs[1].set_xlabel('Time Horizon')  # Replace 'X-axis Label' with your actual x-axis label
            axs[1].set_ylabel('P(win|not play)')
            axs[1].legend()


            dp_means = np.nan_to_num(pwp_means - pwnp_means)
            dp_stds = np.nan_to_num(pwp_stds - pwnp_stds)

            axs[2].plot(x, dp_means,  label="dP={}".format(np.round(PARAMS[0]-PARAMS[1], 4)))
            axs[2].fill_between(x, dp_means-dp_stds, dp_means+dp_stds, alpha=0.2)
            #axs[2].set_title("dP")
            axs[2].set_xlabel('Time Horizon')  # Replace 'X-axis Label' with your actual x-axis label
            axs[2].set_ylabel('dP')
            axs[2].legend()

            list_play = np.asarray(list_play)
            _, m = np.shape(list_play)
            p_play_mean = np.asarray(([np.nanmean(list_play[:, j]) for j in range(m)]))
            p_play_std = np.asarray(([np.nanstd(list_play[:, j]) for j in range(m)]))
            mean = np.nanmean(p_play_mean)
            std = np.nanmean(p_play_std)
            axs[3].bar(index[k], (mean), yerr=std)
            #axs[3].set_title("P(Play)")
            axs[3].legend()
            axs[3].set_xlabel('Agents')  # Replace 'X-axis Label' with your actual x-axis label
            axs[3].set_ylabel('P(Play)')

        
def plot_comparison_causal_estimates(actions, env, params, agents):

    agents = agents #[AIAgent, TSAgent, OCTSAgent, Agent]
    envs = [env(params) for i in range(len(agents))]
    
    fig, axs = plt.subplots(1, 1, figsize=(8,5))

    with warnings.catch_warnings():

        warnings.simplefilter("ignore")   

        for k in range(len(agents)):

            current_env = envs[k]

            observation = {'X': 0, 'Y': 0, 'Z': 0}

            list_pwp = []
            list_pwnp = []
            list_play = []

            for i in tqdm(range(100)):

                current_agent = agents[k](actions)
                
                hist_observations = []
                hist_randag_rewards = []
                hist_randag_actions = []
                observation = current_env.reset()

                previous_action = current_agent.actions[np.random.randint(len(current_agent.actions))]

                for t in range(40):

                    if (str(current_agent).find("AIAgent") > 0 ):
                        action = current_agent.choose_action(observation, previous_action)
                        previous_action = action
                    else:
                        action = current_agent.choose_action(observation)
                        
                    observation, reward, done, info = current_env.step(action)
                    hist_randag_rewards.append(reward)
                    hist_randag_actions.append(action)
                    

                randag_pwp, randag_pwnp, p_play = compute_probs(hist_randag_rewards, hist_randag_actions)
                list_pwp.append(randag_pwp)
                list_pwnp.append(randag_pwnp)
                list_play.append(p_play)

            list_pwp = np.asarray(list_pwp)
            list_pwnp = np.asarray(list_pwnp)
            _, m = np.shape(list_pwnp)
            _, m = np.shape(list_pwp)
            
            pwp_means = np.asarray(([np.nanmean(list_pwp[:,j]) for j in range(m)]))
            pwp_stds = np.asarray(([np.nanstd(list_pwp[:,j]) for j in range(m)]))
           
            pwnp_means = np.asarray(([np.nanmean(list_pwnp[:,j]) for j in range(m)]))
            pwnp_stds = np.asarray(([np.nanstd(list_pwnp[:,j]) for j in range(m)]))

            pwnp_means = np.nan_to_num(pwnp_means)
            pwnp_stds = np.nan_to_num(pwnp_stds)

            dp_means = np.nan_to_num(pwp_means - pwnp_means)
            dp_stds = np.nan_to_num(pwp_stds - pwnp_stds)

            x = np.arange(m)

            axs.plot(x, dp_means,  label="{}".format(current_agent.__name__()))
            axs.fill_between(x, dp_means-dp_stds, dp_means+dp_stds, alpha=0.2)

            #if current_env.__name__() == "BernoulliCausalBandit"
            axs.plot(x, ((params[1]-params[0]))*np.ones(np.shape(x)))
            axs.set_title("dP")
            axs.legend()
    
def plot_cumulative_regrets_bandit(agents, envs):
    PARAMS = [0.6,0.4]
    ACTIONS = [("X",0),("X",1)]

    agents = agents #[AIAgent(ACTIONS), TSAgent(ACTIONS), OCTSAgent(ACTIONS), Agent(ACTIONS)]#, AIBanditAgent(ACTIONS, 1.0)]
    envs = envs #[BernoulliBandit(PARAMS) for i in range(len(agents))]
    regrets = [[] for i in range(len(agents))]
    cumul_reg = []

    for i in (range(len(agents))): 
        current_agent = agents[i]
        current_env = envs[i]

        previous_action = ACTIONS[np.random.randint(2)]
        current_cumul_reg = []
        current_regret = []

        for t in tqdm(range(1000)):
            observation = current_env.reset()
            for k in range(40):
                if i == 0:  # Supposons que 'i' est défini quelque part dans votre code
                    action = current_agent.choose_action(observation, previous_action)
                    previous_action = action
                else:
                    action = current_agent.choose_action(observation)
                observation, reward, done, info = current_env.step(action)

                # Ajouter le regret cumulatif pour cet essai
                current_regret.append(current_env.regrets[-1])  # Supposant que current_env.regrets est mis à jour après chaque step
                current_cumul_reg.append(np.sum(current_regret))  # Cumul des regrets jusqu'à présent

        reshaped_data = np.array(current_cumul_reg).reshape(40, 1000).T  # Remarque: la forme devrait être (40, 1000), non (1000, 40)
        _, m = reshaped_data.shape

        # Calculer les moyennes et les écarts types
        means = np.mean(reshaped_data, axis=0)
        stds = np.std(reshaped_data, axis=0)
        
        x = np.arange(m)

        # Tracer les moyennes
        plt.plot(x, means, label='Moyenne')

        # Ajouter les barres d'erreur pour les écarts types
        plt.errorbar(x, means, yerr=stds, capsize=5, label='Écart type')

        # Ajouter les titres et les labels
        plt.title("Moyennes et Écarts Types par Étape")
        plt.xlabel("Étape")
        plt.ylabel("Regret Cumulatif Moyen")
        

        # Afficher le graphique
    

    plt.legend(['Active Inference',  'TS', 'OCTS',  'random'])
    plt.title('Cumulative Regrets - Bernoulli Bandit')

NX = 5000
def generate_cumulative_regrets_causal_bandit(agents, envs, N=NX):
    PARAMS = [0.9,0.1,0.6,0.4, 0.5]
    ACTIONS = [("X",0),("X",1)]

    agents = agents #[AIAgent(ACTIONS), TSAgent(ACTIONS), OCTSAgent(ACTIONS), Agent(ACTIONS)]#, AIBanditAgent(ACTIONS, PARAMS[4])]
    envs = envs #[BernoulliBandit(PARAMS) for i in range(len(agents))]
    regrets = [[] for i in range(len(agents))]
    final_regrets = [[] for _ in agents]  # Initialize final_regrets to store the final regret for each agent

    for i in tqdm(range(len(agents))):

        agents = agents #[AIAgent(ACTIONS), TSAgent(ACTIONS), OCTSAgent(ACTIONS), Agent(ACTIONS)]
        current_agent = agents[i]
        current_env = envs[i]
        current_regret = []  # Initialize an empty list to store the regrets for each trial

        previous_action = ACTIONS[np.random.randint(2)]

        for t in range(N):
            observation = current_env.reset()
            for k in range(40):
                if (i == 0):
                    action = current_agent.choose_action(observation, previous_action)
                    previous_action = action
                else:
                    action = current_agent.choose_action(observation)
                observation, reward, done, info = current_env.step(action)
            
            # Append the final cumulative regret after 40 steps
            current_regret.append(np.sum(current_env.regrets))
        
        #current_cumul_regret = np.cumsum(current_regret, axis=0)
        
        # Convert the list of regrets to a numpy array
        current_regret_array = np.array(current_regret)

        # Store the final regrets for the current agent
        final_regrets[i] = current_regret_array

    return np.array(final_regrets)

def plot_cumulative_regrets_causal_bandit(agents, envs):
    PARAMS = [0.9,0.1,0.6,0.4, 0.5]
    ACTIONS = [("X",0),("X",1)]

    agents = agents #[AIAgent(ACTIONS), TSAgent(ACTIONS), OCTSAgent(ACTIONS), Agent(ACTIONS)]#, AIBanditAgent(ACTIONS, PARAMS[4])]
    envs = envs #[BernoulliCausalBandit(PARAMS) for i in range(len(agents))]
    regrets = [[] for i in range(len(agents))]

    for i in tqdm(range(len(agents))): 
        current_agent = agents[i]
        current_env = envs[i]
        current_regret = regrets[i]

        previous_action = ACTIONS[np.random.randint(2)]

        for t in range(1000):
            observation = current_env.reset()
            for k in range(40):
                if (i==0):
                    action = current_agent.choose_action(observation, previous_action)
                    previous_action = action
                else:
                    action = current_agent.choose_action(observation)
                observation, reward, done, info = current_env.step(action)
            current_regret.append(current_env.regrets)
        
        current_cumul_reg = np.cumsum(current_regret, axis=0)
        _,m = np.shape(current_cumul_reg)
        means = np.asarray([np.mean(current_cumul_reg[j, :]) for j in range(m)])
        stds = np.asarray([np.std(current_cumul_reg[j, :]) for j in range(m)])
        x = np.arange(m)

        plt.plot(x, means)
        plt.fill_between(x, means - stds, means + stds, alpha = 0.2, label='_nolegend_')

    plt.legend(['Active Inference',  'TS', 'OCTS',  'random', 'AI Bandit'])
    plt.title('Cumulative Regrets - Causal Bandit')
    plt.tight_layout()

N = 5000
def generate_cumulative_regrets_causal_bandit(agents,envs):
    PARAMS = [0.9,0.1,0.6,0.4, 0.5]
    ACTIONS = [("X",0),("X",1)]

    agents = agents #[AIAgent(ACTIONS), TSAgent(ACTIONS), OCTSAgent(ACTIONS), Agent(ACTIONS)]#, AIBanditAgent(ACTIONS, PARAMS[4])]
    envs = envs #[BernoulliCausalBandit(PARAMS) for i in range(len(agents))]
    regrets = [[] for i in range(len(agents))]
    final_regrets = [[] for _ in agents]  # Initialize final_regrets to store the final regret for each agent

    for i in tqdm(range(len(agents))):

        agents = agents # [AIAgent(ACTIONS), TSAgent(ACTIONS), OCTSAgent(ACTIONS), Agent(ACTIONS)]
        current_agent = agents[i]
        current_env = envs[i]
        current_regret = []  # Initialize an empty list to store the regrets for each trial

        previous_action = ACTIONS[np.random.randint(2)]

        for t in range(N):
            observation = current_env.reset()
            for k in range(40):
                if (i == 0):
                    action = current_agent.choose_action(observation, previous_action)
                    previous_action = action
                else:
                    action = current_agent.choose_action(observation)
                observation, reward, done, info = current_env.step(action)
            
            # Append the final cumulative regret after 40 steps
            current_regret.append(np.sum(current_env.regrets))
        
        #current_cumul_regret = np.cumsum(current_regret, axis=0)
        
        # Convert the list of regrets to a numpy array
        current_regret_array = np.array(current_regret)

        # Store the final regrets for the current agent
        final_regrets[i] = current_regret_array

    return np.array(final_regrets)


def compute_probs_conf(arg_rewards, arg_actions):

    with warnings.catch_warnings():

        warnings.simplefilter("ignore")

        actions = [action for action in arg_actions if action[0] == "X"]
        rewards = [reward for (action, reward) in zip(arg_actions, arg_rewards) if action[0] == "X"]

        # compute probability to win when the agent's play
        win_play = [((action[1] and reward)) for (action, reward) in zip(actions, rewards)]
        num_win_play = [np.sum(win_play[:i]) for i in range(len(win_play))]
        num_play = [np.sum([action[1] for action in actions[:i]]) for i in range(len(actions))]
        p_win_play = [win_play_t/play_total_t for (win_play_t, play_total_t) in zip(num_win_play, num_play)]

        # compute the probability to win when the agent doesn't play
        win_no_play = [int(not(action[1]) and reward) for (action, reward) in zip(actions, rewards)]
        num_win_no_play = [np.sum(win_no_play[:i]) for i in range(len(win_no_play))]
        num_no_play = [np.sum([int(not(action[1])) for action in actions[:i]]) for i in range(len(actions))]
        p_win_no_play = [win_no_play_t/no_play_t for (win_no_play_t, no_play_t) in zip(num_win_no_play, num_no_play)]

        # compute probability of play
        p_win_play = [(0.5 if np.isnan(p) else p) for p in p_win_play]
        p_win_no_play = [(0.5 if np.isnan(p) else p) for p in p_win_no_play]

        p_play = [num_play/i for (i, num_play) in enumerate(num_play)]

        return p_win_play, p_win_no_play, p_play




def compute_p_play(agent_name, reset_agent=True):

    list_params = [[0.2, 0.8, 0.3, 0.7, 0.6, 0.9, 0.1]]
                    #[0.7, 0.3, 0.3, 0.7, switch],
                    #[0.5, 0.5, 0.5, 0.5, switch],
                    #[0.3, 0.7, 0.7, 0.3, switch]]
    p_play_mean = []
    p_play_std = []
    ACTIONS = [("X",0),("X",1), ("Z", 0), ("Z", 1)]

    for k in range(0,len(list_params)):

        with warnings.catch_warnings():

            warnings.simplefilter("ignore") 

            PARAMS = list_params[k]
            env = BernoulliCausalBandit(PARAMS)
            observation = env.reset()  

            if not(reset_agent):
                agent = agent_name(ACTIONS)

            list_play = []

            for i in tqdm(range(1000)):

                hist_observations = []
                hist_ag_rewards = []
                hist_ag_actions = []

                observation = env.reset()

                
                agent = agent_name(ACTIONS)
                    
                previous_action = agent.actions[np.random.randint(len(agent.actions))]

                for k in range(40):
                    action = agent.choose_action(observation, previous_action)
                    observation, reward, done, info = env.step(action) #change here
                    hist_ag_rewards.append(reward)
                    hist_ag_actions.append(action) 
                    previous_action = action
                    
                #for k in range(40):    
                #    action = agent.choose_action(observation)
                #    observation, reward, done, info = env.step(action)
                #    hist_ag_rewards.append(reward)
                #    hist_ag_actions.append(action) 
                #    previous_action = action

                #for t in range(40):
                #    if (t == 20 ):
                #        observation = env.reset()

                #    if  agent.__name__() == "AIAgent":
                #        action = agent.choose_action(observation, previous_action)
                #        previous_action = action
                #    else:
                #        action = agent.choose_action(observation)
                #    observation, reward, done, info = env.step(action)

                #    hist_ag_rewards.append(reward)
                #    hist_ag_actions.append(action) 


                _, _, p_play = compute_probs(hist_ag_rewards, hist_ag_actions)
                
                list_play.append(p_play)

            list_play = np.asarray(list_play)
            _, m = np.shape(list_play)
            p_play_mean.append(np.asarray(([np.nanmean(list_play[:, j]) for j in range(m)])))
            p_play_std.append(np.asarray(([np.nanstd(list_play[:, j]) for j in range(m)])))

    return p_play_mean, p_play_std

