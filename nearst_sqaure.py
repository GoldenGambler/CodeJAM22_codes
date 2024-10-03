import math

def forward(i):
        while math.sqrt(i)%1!=0:
            i+=1
        else:
            return i
    
def backward(i):
        while math.sqrt(i)%1!=0:
            i-=1
        else:
            return i

def decide():
    for i in a:
        if (forward(i)-i)>(i-backward(i)):
            b.append(backward(i))
        else:
            b.append(forward(i))
    print(b)    
    

a=eval(input("Enter a list of numbers"))
a=list(a)
b=[]
if len(a)>=2 and len(a)<=100:
    for i in a:
        if 1>i and i>1000:
            print("Sorry bro the numbers too big or too small in the list ")
    else:
        decide()
else:
    print("The len of the list should be in the range of 2 to 100")
