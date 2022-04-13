import os
import ast
from collections import Counter
import csv
import pandas as pd
from radon.visitors import ComplexityVisitor

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
    return Counter(functionCount).values()

df["WMC"]=WeightedMethodPerClass()

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
    for file in files:
        if os.path.isfile(os.path.join(pathOfFolderToRead, file)):
            f = open(os.path.join(pathOfFolderToRead, file), 'r')
            tree = ast.parse(f.read())
            print(sum(isinstance(exp, ast.FunctionDef) for exp in tree.body))
            method_count = sum(isinstance(exp, ast.FunctionDef) for exp in tree.body)
    return method_count

df["NAM"]=NumberOfAccessMethod()

def NumberOfComments():
    """
        purpose: the number of comments
        Args: No input paramemter, just read all the files in pathOfFolderToRead folder name
        Returns: number of classes to which a class is coupled
    """
    ListOfCommentcount = []
    for file in files:
        if os.path.isfile(os.path.join(pathOfFolderToRead, file)):
             f = open(os.path.join(pathOfFolderToRead, file), 'r')
             ListOfCommentcount.append(len([line for line in f if line.strip().startswith('#')]))
    return ListOfCommentcount

df["NOC"] = NumberOfComments()


def NumberOfStaticImports():
    """
    purpose: the number of static Imports
    Args: No input paramemter, just read all the files in pathOfFolderToRead folder name
    Returns: number of classes to which a class is coupled
    """
    ListOfStaticImport =[]
    for file in files:
        if os.path.isfile(os.path.join(pathOfFolderToRead, file)):
            f = open(os.path.join(pathOfFolderToRead, file), 'r')
            ListOfStaticImport.append(len([line for line in f if line.strip().count('import')]))
    return ListOfStaticImport

df["NOSI"]=NumberOfStaticImports()

def RatioOfCommentToCode():
    """
            purpose: give insight regarding the ratio of documentation to logic code
            Args: No input paramemter, just read all the files in pathOfFolderToRead folder name
            Returns: number of classes to which a class is coupled
        """
    df["RCC"] = df.apply(lambda row: row.NOC + row.LOC, axis=1)

RatioOfCommentToCode()

def CyclomaticComplexity():
    """
                purpose: give insight regarding the overall Compplexity of logic code (Macabe's Index measue)
                Args: No input paramemter, just read all the files in pathOfFolderToRead folder name
                Returns: number of classes to which a class is coupled
    """
    for file in files:
        if os.path.isfile(os.path.join(pathOfFolderToRead, file)):
            f = open(os.path.join(pathOfFolderToRead, file), 'r')
            lines = f.readlines()
            # for ind, line in enumerate(lines):
            #     num_of_chars = len(line) - len(line.lstrip())  # Get the preceding characters.
            #     new_line = line[:num_of_chars]
            #     lines[ind] = new_line
            data = ' '.join([line.replace('\n', '') for line in f.readlines()])
            v = ComplexityVisitor.from_code(str(data))
            print(v.complexity)
    return v.complexity

df["CC"]=CyclomaticComplexity()

print(df)
df.to_csv("Outcome.csv")