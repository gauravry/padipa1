# Standard deviation mean and correletion calculation ##

import math

def mean(list_in):
    x = len(list_in)
    return sum(list_in)/x


def stdDev(list_in):
    x = len(list_in)
    y = [((list_in[i]-mean(list_in))**2) for i in range(x)]
    #print("y",y)
    #print(sum(y))
    return math.sqrt((sum(y)/(x)))


def correl_ret(list1,list2):
    x = len(list1)
    cor1 = []
    cor2 = []
    cor3 = []

    cor1 = [(list1[i]-mean(list1)) for i in range(x)]
    cor2 = [(list2[i]-mean(list2)) for i in range(x)]
    cor3 = [(cor1[i]*cor2[i]) for i in range(x)]
    #print(cor1)
    #print(cor2)
    #print(cor3)
    num = sum(cor3)
    dem = x*stdDev(list1)*stdDev(list2)
    res = num/dem
    return res

def uniq_test(list_in):
    unq_list=[]

    for x in list_in:
        # check with if
        if x not in unq_list:
            unq_list.append(x)
    return unq_list
num = int(input())

n1 = list(map(float, input().split()))
n2 = list(map(float, input().split()))

if (len(n1) == num and len(n2) ==num):
    if len(n1) == len(uniq_test(n1)):
        if len(n2) == len(uniq_test(n2)):
            print(correl_ret(n1,n2))
        else:
            print("n2 not uniq")
    else:
        print("n1 not uniq")
else:
    print("num not matching n1 and n2")
