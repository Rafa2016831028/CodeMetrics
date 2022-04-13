import os
from inspect import getmembers, isfunction, isclass
import ast
import inspect
from collections import Counter
import csv
import pandas as pd

pathOfFolderToRead = 'static'
files = os.listdir(pathOfFolderToRead)
keyword = 'def'

df = pd.DataFrame()
df["FileName"] = files


def WeightedMethodPerClass():
    """
       purpose: (WMC) Weighted Methods Per Class
       Args: No input paramemter, just read all the files in pathOfFolderToRead folder name
       Returns:
            number of methods defined in class
       """
    functionCount = [];
    for file in files:
        if os.path.isfile(os.path.join(pathOfFolderToRead, file)):
            f = open(os.path.join(pathOfFolderToRead, file), 'r')

            for x in f:
                if keyword in x:
                    functionCount.append(f.name)
            f.close()
    return functionCount


print(WeightedMethodPerClass())


# def CBO():
#     """
#            purpose:  Coupling between Object Classes
#            Args: No input paramemter, just read all the files in pathOfFolderToRead folder name
#            Returns: number of classes to which a class is coupled
#     """
#     from static import utils
#     from static import trail
#     import numpy as np
#
#     methodNameArray1 = [];
#     methodNameArray2= [];
#
#     val1 = getmembers(utils, isfunction)
#     for val in val1:
#         methodNameArray1.append(val[0])
#     val2 = getmembers(trail, isfunction)
#     for val in val2:
#         methodNameArray2.append(val[0])
#     common_elements = np.intersect1d(methodNameArray1, methodNameArray2)
#     print(len(common_elements))
#
# CBO()

def LineOfCode():
    """
    purpose:  Counting the number of lines changed
    Args: No input paramemter, just read all the files in pathOfFolderToRead folder name
    Returns: number of classes to which a class is coupled
    """
    ListOfLOCcount = []
    for file in files:
        if os.path.isfile(os.path.join(pathOfFolderToRead, file)):
            f = open(os.path.join(pathOfFolderToRead, file), 'r')
            ListOfLOCcount.append(sum(1 for _ in f))
    return ListOfLOCcount


df["LOC"] = LineOfCode()


def NumberOfAccessMethod():
    """
    purpose: parse the file changes to extract the number of access method call
    Args: No input paramemter, just read all the files in pathOfFolderToRead folder name
    Returns: number of classes to which a class is coupled
    """
    method_count = []
    for file in files:
        if os.path.isfile(os.path.join(pathOfFolderToRead, file)):
            f = open(os.path.join(pathOfFolderToRead, file), 'r')
            tree = ast.parse(f.read())
            print(sum(isinstance(exp, ast.FunctionDef) for exp in tree.body))
            method_count.append(sum(isinstance(exp, ast.FunctionDef) for exp in tree.body))
            return method_count


print(NumberOfAccessMethod())


# df["NAM"]=NumberOfAccessMethod()

def NumberOfComments():
    """
                 purpose: the number of comments
                 Args: No input paramemter, just read all the files in pathOfFolderToRead folder name
                 Returns: number of classes to which a class is coupled
            """
    for file in files:
        if os.path.isfile(os.path.join(pathOfFolderToRead, file)):
            f = open(os.path.join(pathOfFolderToRead, file), 'r')
            return len([line for line in f if not line.strip().startswith('#')])


df["NOC"] = NumberOfComments()


def NumberOfStaticImports():
    """
                 purpose: the number of static Imports
                 Args: No input paramemter, just read all the files in pathOfFolderToRead folder name
                 Returns: number of classes to which a class is coupled
            """
    for file in files:
        if os.path.isfile(os.path.join(pathOfFolderToRead, file)):
            f = open(os.path.join(pathOfFolderToRead, file), 'r')
            return len([line for line in f if not line.strip().startswith('import')])


df["NOSC"] = NumberOfStaticImports()

print(df)