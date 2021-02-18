import math
n = int(input())
mu = int(input())
stdev = int(input())
prob_req = float(input())
z = float(input())


A = mu + (1.96*(stdev/math.sqrt(n)))
B = mu - (1.96*(stdev/math.sqrt(n)))

print(round(A,2))
print(round(B,2))
