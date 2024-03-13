from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements
    

"""file_path: str: This is the input parameter to the function, 
and it is annotated with the type hint str, indicating that the function expects a string representing a file path."""

"""-> List[str]: This part of the signature indicates the return type of the function. 
It specifies that the function will return a list of strings (List[str])."""

"""The purpose of the get_requirements function is to read a requirements file (usually named 'requirements.txt') and extract the dependencies listed in that file. 
The function opens the file, reads its lines, removes newline characters from each line, and then processes the requirements"""



setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='KevalSanghani',
    author_email='kevalpatel0103@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()
)
