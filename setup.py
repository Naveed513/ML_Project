from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns the required packages list
    '''
    with open(file_path) as file_obj:
        requirements = [line.replace('\n','') for line in file_obj.readlines() if HYPEN_E_DOT not in line]

    return requirements

setup(
    name = 'ML_Project',
    version = '0.0.1',
    author = 'Naveed',
    author_email =  'sknaveed513@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)