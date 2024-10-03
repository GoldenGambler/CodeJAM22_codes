from datetime import datetime

def value_fixer(a):
    a1=''
    for i in a:
        if i.isnumeric()==False:
            a1+=":"
        else:
            a1+=i
    return a1

def to_pos(a):
    if a<0:
        return a*-1
    else:
        return a  

def what_i_want(x):
    t=0
    c=0
    for i in l:
        if t+i<x:
            t+=i
            c+=1
        else:
            break
    return c

def real_stuff():
    if n<4 or n>100:
        print("Nah bro enter with in 4 to 100 range ")
    else:
        print("Enter start and end time for each activity in 24 hr format ")
        for i in range(n):
            print("Round",(i+1))
            a=value_fixer(input("Enter start time and"))
            b=value_fixer(input("Enter end time "))
            print()
            l.append(to_pos(int(b)-int(a)))
        l.sort()
        print(what_i_want(y))


y=eval(input("Enter time free to work on activities "))
if y>24:
    print("You cant enter more than 24 hrs ")
else:
    n=int(input("Enter your number of activities "))
    l=[]
    real_stuff()
