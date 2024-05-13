import numpy as np
import pandas as pd
def Linear_Max_Min(attribute, Type):
   
    MIN = min(attribute)
    MAX = max(attribute)
    Var = MAX - MIN
    attribute = np.array(attribute)
    if Type == "profit":
        Attribute = (attribute - MIN)/Var
    elif Type == "cost":
        Attribute = (MAX - attribute)/Var
    
    return Attribute

def Linear_Max(attribute, Type):
    
    MAX = max(attribute)
    attribute = np.array(attribute)
    if Type == "profit":
        Attribute = attribute/MAX
    elif Type == "cost":
        Attribute = 1 - attribute/MAX
    
    return Attribute

def Linear_sum(attribute, Type):
    
    SUM_1 = sum(attribute)
    SUM_2 = sum(1/attribute)
    attribute = np.array(attribute)
    if Type == "profit":
        Attribute = attribute/SUM_1 
    elif Type == "cost":
        Attribute = (1/attribute)/SUM_2
        
    return Attribute


def Vector_Normalization(attribute, Type):
   
    r = (sum(attribute**2))**(0.5)
    if Type == "profit":
        Attribute = attribute/r 
    elif Type == "cost":
        Attribute = 1 - attribute/r 
        
    return Attribute


def Logarithmic_normalisation(attribute, Type):
   
    r = np.log(np.prod(attribute))
    if Type == "profit":
        Attribute = np.log(attribute)/r
        
    if Type == "cost":
        Attribute = (1 - (np.log(attribute)/r))/(len(attribute)-1)
        
    return Attribute



                          
