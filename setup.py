from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.

    '''
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]

    return requirements


setup(
name='MedicinePredictor',
version='0.0.1',
author='Victor Brancus',
author_email='vbrancus99@gmail.com',
description='Search methods of small molecules interaction with 3 protein targets.',
long_description=open('README.md').read(),
url='https://github.com/vbrancus99/Leash-Bio-Predict-New-Medicines-with-BELKA',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)