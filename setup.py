from setuptools import setup, find_packages

# Install with 'pip install -e .'

setup(
    name="gym_cassie_run",
    version="0.1.1",
    author="Nicolas Perrin-Gilbert",
    description="gym(nasium) RL environment in which a mujoco simulation of"
    "Agility Robotics' Cassie robot is rewarded for walking forward",
    url="https://github.com/perrin-isir/gym-cassie-run",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.5",
        "gymnasium>=0.28.1",
        "mujoco>=2.2.2",
        "Pillow>=9.0.1",
        "ipywidgets>=7.6.5",
        "mediapy>=1.1.4",
    ],
    license="LICENSE",
)
