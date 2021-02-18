import numpy 

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],float)
#A = numpy.array([[1,2],[3,4]],dtype=int)
z0=(numpy.mean(A,axis=1))  #Axis 1
z1=(numpy.var(A,axis=0))  #Axis 1
z3=(numpy.std(A,))  #Axis 1


print(z0)
print(z1)
print(z3)
