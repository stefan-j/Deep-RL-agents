
import os

import numpy as np

import settings

def save(saver, fig_name):
    for path, data in saver:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        data = " ".join(map(str, data))
        with open(path, "w") as file:
            file.write(data)


def mean(tab, step=10):
    return [np.mean(tab[max(1, i - step):i]) for i in range(2, len(tab))]


class Displayer:

    def __init__(self):
        self.rewards = [[] for a in range(settings.NB_ACTORS + 1)]
        self.sequential_rewards = []
        self.q_buf = []

    def add_reward(self, reward, n_agent, plot=False):
        self.rewards[n_agent].append(reward)
        if n_agent != 0:
            self.sequential_rewards.append(reward)
        if plot:
            print(self.rewards[1][max(0, -50):])


DISPLAYER = Displayer()
