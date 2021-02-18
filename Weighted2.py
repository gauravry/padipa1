def do_stuff():
    print(arr)
    print(arr2)
    num=float(sum(arr*arr2))
    den = float(sum(arr2))
    xx = num/den
    print(type(xx))
    print(round(xx,1))

n = int(input("enter size :"))
arr= np.array(input().split(),dtype=int)
arr2= np.array(input().split(),dtype=int)
x = arr.size
print("arr:",arr)
print("arr2:",arr2)
x2 = arr2.size
if (n == x and n == x2):
    if (np.all(np.logical_and(arr > 0, arr < 101))==True):
        print("one")
        if (np.all(np.logical_and(arr2 > 0, arr2 < 101))==True):
            do_stuff()
        else:
            print("Please enter number between arr2 0 and 100")
    else:
        print("Please enter number between arr1 0 and 100")
else:
    print("Please enter",n,"numbers")
