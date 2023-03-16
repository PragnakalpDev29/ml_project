from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requiers(file_path:str)->List[str]:
    '''
    will return list of req
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='ml_projects',
version='0.0.0.1',
author='Dhyanesh',
packages=find_packages(),
install_requires=get_requiers('requirements.txt')




)