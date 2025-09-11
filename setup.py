##packaging the entire content
'''
the setup.py file is an essential part of packaging and distributing python projects. it is used by setup tools
(or distutils in older python versions) to define the configuration of your project,such as its metadata, dependencies,
and more'''

from setuptools import setup, find_packages,setup 
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement_list:[str]=[]
    with open('requirements.txt') as file:
        lines=file.readlines()

        for line in lines:
            requirement = line.strip()
            ##ignore empty lines and -e.
            if requirement and requirement != '-e.':
                requirement_list.append(requirement)
    return requirement_list