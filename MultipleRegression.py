from pandas.core.frame import DataFrame
import scipy as sp
import pandas as pd 
import numpy as np
import math
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import linear_model
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

x1 = np.array([3,4,6,8,9])
x2 = np.array([1,1,3,6,4])
x3 = np.array([2,2,5,6,9])
y =  np.array([2,3,6,5,8])
print("old",x1.shape)
print("old",type(x1))

xn1 = x1.reshape(-1,1)
print("new",xn1.shape)
print("new",type(xn1))
xn2 = x2.reshape(-1,1)
xn3 = x3.reshape(-1,1)

print(xn1)
print(xn1)
print(xn3)
X = np.concatenate((xn1,xn2,xn3),axis=1)
print(X)
yn1 = y.reshape(-1,1)

reg = linear_model.LinearRegression()
reg.fit(X,y)
print(reg.coef_)
print(reg.intercept_)
