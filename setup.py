from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    """This function will return the list of requirements"""
    get_requirements = []
    with open(file_path) as requirement_file:
        get_requirements=requirement_file.readlines()
        get_requirements=[req.replace("\n","") for req in get_requirements]
        if HYPEN_E_DOT in get_requirements:
            get_requirements.remove(HYPEN_E_DOT)
    


setup(
    name="student_placement_prediction",
    version="0.1.0",
    author="sachin jangir",
    author_email="sachinjangir1319@gmail.com",
    description="A machine learning project to predict student placement",
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt'),
)