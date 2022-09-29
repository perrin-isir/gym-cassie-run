from setuptools import setup, find_packages

# Install with 'pip install -e .'

setup(
    name="gym_cassie_run",
    version="0.1.0",
    author="Nicolas Perrin-Gilbert",
    description="gym RL environment in which a mujoco simulation of Agility Robotics' "
    "Cassie robot is rewarded for walking forward",
    url="https://github.com/perrin-isir/gym-cassie-run",
    packages=find_packages(),
    install_requires=[
        "gym>=0.26.0",
        "mujoco>=2.2.2",
    ],
    license="LICENSE",
)
