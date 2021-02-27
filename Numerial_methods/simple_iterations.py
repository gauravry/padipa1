import math
x = 2

def for_loop(x):
    for iteration in range(1,101):
        #xnew = (2*x**2 + 3)/5
        xnew = math.sqrt((5*x-3)/2)
        if abs(xnew -x) < 0.000001:
            break
        print(x,xnew,iteration)
        x=xnew
    return xnew

y1 = 5
y2 = 0
iter1 = 0

def while_loop(y1,y2,iter1):
    while abs(y2-y1) >= 0.000001:
        iter1 +=1
        y1 = y2
        y2 = (2*y1**2 + 3)/5
    return y2,iter1


x2=for_loop(x)
print('the root %0.5f' %x2)

y1 = 5
y2 = 0
iter1 = 0
y3,iter1 = while_loop(y1,y2,iter1)
print('the root %0.5f iter'  %y3, 'test %d' %iter1)
