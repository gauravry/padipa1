import numpy as np
import math
from numpy.core.fromnumeric import mean
from scipy import stats

from numpy.lib.function_base import average, median

### This will return the middle index if odd and middle two values if even

def return_med_index(m):
    rolls = np.empty(3)
    if m % 2 == 0:
        rolls[0] = m // 2
        rolls[1] = (m // 2) -1
        print("rolls0",rolls[0])
        print("rolls1",rolls[1])
        return rolls[0:2]
    else:
        rolls[0] = m // 2
        return rolls[0:1]
#This prints the result
def do_stuff():
    rolls = np.array(return_med_index(x))
    rolls = rolls.astype(int)
    #print(arr)
    arr.sort()
    s0 = mean(arr)
    s1 = mean(arr[rolls])
    s2 = stats.mode(arr)[0].astype(float)[0]
    print(round(s0,1))
    print(round(s1,1))
    print(round(s2,1))


n = int(input())
arr= np.array(input().split(),dtype=int)
x = arr.size
if n == arr.size:
    #print("d")
    #print("check",np.all(np.logical_and(arr1 > 10, arr1 < 15)))
    if (np.all(np.logical_and(arr < 10, arr < pow(10,5)))==True):
        print("Please enter number between 10 and powe(10,5)")
    else:
        do_stuff()
else:
    print("Please enter",n,"numbers")









    #if (np.all(np.logical_and(arr1 > 10, arr1 < 15))==True):
     #   print("x")
    #else:

# print(arr1)
# a_bool = np.any(arr1)
# print(a_bool)

# b_bool = np.all(arr1)
# print(b_bool)

# c_bool =np.where(arr1<10)
# c_bool = np.array(c_bool)
# print(c_bool.size)
# print(c_bool)




