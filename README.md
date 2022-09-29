# gym-cassie-run
RL environment (with OpenAI Gym interface) in which a mujoco simulation of Agility Robotics' Cassie robot is rewarded for walking/running forward as fast as possible.

The Cassie model is the one available in DeepMind's [mujoco_menagerie](https://github.com/deepmind/mujoco_menagerie), and the gym environment is inspired from 
[HalfCheetah-v4](https://github.com/openai/gym/blob/master/gym/envs/mujoco/half_cheetah_v4.py). In addition to the basic reward for forward motion, hand-designed reward signals 
encourage walking rather than jumping, keeping feet horizontal and not too far apart, and avoiding lateral movements.

The following episode has been obtained after training a [TQC](https://arxiv.org/abs/2005.04269) agent for 17M timesteps, using the [xpag](https://github.com/perrin-isir/xpag) RL platform:

![](episode.gif)


## Installation

<details><summary>Option 1: pip</summary>
<p>

    pip install git+https://github.com/perrin-isir/gym-cassie-run

</p>
</details>

<details><summary>Option 2: conda</summary>
<p>

    git clone https://github.com/perrin-isir/gym-cassie-run.git
    cd gym-cassie-run

Choose a conda environmnent name, for instance `cassierunenv`.  
The following command creates the `cassierunenv` environment with the requirements listed in [environment.yaml](environment.yaml):

    conda env create --name cassierunenv --file environment.yaml

If you prefer to update an existing environment (`existing_env`):

    conda env update --name existing_env --file environment.yml

To activate the `cassierunenv` environment:

    conda activate cassierunenv

Finally, to install the *gym-cassie-run* library in the activated virtual environment:

    pip install -e .

</p>
</details>

Once the installation is complete, you can import the environment in python with:  
```import gym_cassie_run```  
This directly registers the environment *CassieRun-v0* in gym.