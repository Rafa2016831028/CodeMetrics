import os
from inspect import getmembers, isfunction, isclass
import ast
from collections import Counter

pathOfFolderToRead = 'static'
files = os.listdir(pathOfFolderToRead)
keyword = 'def'


def WMC():
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
    return Counter(functionCount)

print(WMC())

def CBO():
    """
           purpose:  Coupling between Object Classes
           Args: No input paramemter, just read all the files in pathOfFolderToRead folder name
           Returns: number of classes to which a class is coupled
    """
    from static import utils
    from static import trail_again
    import numpy as np

    methodNameArray1 = [];
    methodNameArray2= [];

    val1 = getmembers(utils, isfunction)
    for val in val1:
        methodNameArray1.append(val[0])
    val2 = getmembers(trail_again, isfunction)
    for val in val2:
        methodNameArray2.append(val[0])
    common_elements = np.intersect1d(methodNameArray1, methodNameArray2)
    print(len(common_elements))
            # print(file)
            # classes = [x for x in dir(f) if isclass(getattr(f, x))]
            # print(classes)
CBO()



