#!/usr/bin/env python

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='unity_tennis',
      version='0.1.0',
      description='Unity Tennis',
      packages=find_packages(),
      install_requires=required,
      long_description="An implementation of a DDPG agent playing the Unity Tennis Environment."
      )
