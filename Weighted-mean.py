# Number of Variables
n = int(input())
# Enter the variables
nums = [int(x) for x in input().split()]
#Enter the weight of respective Variables
weight = [int(x) for x in input().split()]
#Multiply nums by weight and sum all up
print(round(1.0*sum([nums[i]*weight[i] for i in range(n)])/sum(weight), 1))
