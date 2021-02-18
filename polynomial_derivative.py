import numpy as np
import matplotlib.pyplot as plt


print(np.poly([-1, 1, 1, 10]))
x = np.arange(-10,20,1)
print(x)
print(type(x))
    
# Giving the roots  
seq_1 = (-1,1,1,10) 
a = np.poly(seq_1) 
print ("Coefficients of the polynomial: ", a) 
  
# Constructing polynomial   
p1 = np.poly1d(a) 
pder1 = np.polyder(p1) 
print ("\nAbove polynomial = \n", p1)  

y =p1(x)
x2 = x
y2 = pder1(x)
y3 = x*0

plt.plot(x,y)
plt.plot(x,y2)
plt.plot(x,y3)
#plt.axis('equal')
plt.grid(True)
plt.plot(2,3)
plt.show()
