from setuptools import find_packages,setup
from typing import List

hypen_edot="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hypen_edot in requirements:
            requirements.remove(hypen_edot)

    return requirements

setup(
name='Om Shirsat',
version='0.0.1',
author='Om',
author_email='omshirsat77@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)