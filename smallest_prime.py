def sorter():
    b=[]
    for i in a:
        for j in i:
            b.append(j)
    b.sort()
    return b

def prime(n):
    l=True
    a=n
    for i in range(n-1,1,-1):
        if a%i==0:
            l=False
    return l

def loop(b):
    for i in b:
        x=prime(i)
        if x:
            print(i,"is the smallest prime number ")
            break
    else:
        print("Not found ")

a=eval(input("enter in this form [[],[],[]] "))
if len(a)==3:
    if len(a[0])==3 and len(a[0])==3 and len(a[0])==3:
        loop(sorter())        
    else:
        print("inner elements are not in 3 by 3 form ")
else:
    print("It is not a 3x3 array")
    
