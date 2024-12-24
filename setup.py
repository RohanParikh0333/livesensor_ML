from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_list:List[str] = []
    return requirement_list

setup(
    name='sensor',
    version='1.0.1',
    author='Rohan Parikh',
    author_email='rohanparikh106045@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
    
    
)