from setuptools import find_packages,setup
from typing import List

our_character = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if our_character in requirements:
            requirements.remove(our_character)

    return requirements

setup(
    name='ml-project',
    version = '0.0.1',
    author='Krishna',
    author_email='prakash.spaes@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)