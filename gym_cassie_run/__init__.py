import os
import gymnasium as gym
from gymnasium.envs.registration import register

__version__ = "0.1.1"


def envpath():
    resdir = os.path.join(os.path.dirname(__file__))
    return resdir


print("gym-cassie-run: ")
print("|    gym version and path:", gym.__version__, gym.__path__)

print("|    REGISTERING CassieRun-v0 from", envpath())
register(
    id="CassieRun-v0",
    entry_point="gym_cassie_run.env:CassieRunEnv",
    max_episode_steps=1000,
)
