from setuptools import setup
from typing import List


#Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION =  "0.0.1"
AUTHOR = "Hemant Kadam"
DESCRIPTION = "This is my first machine learning project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement 
    in the requirements.txt file
    
    returns : This function is going to return a list which will contain name 
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
       return  requirement_file.readline()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires= get_requirements_list()

)
