low=None
max=None
l=[]
pr=[]

def sorting(k):
    k=list(k)
    k.sort()
    k.reverse()
    k="".join(k)
    return k

def first_n_last(k):
    low=k[-2]
    max=k[:len(k)-1]
    getting_list(low,max)
            
def getting_list(low,max):
    for i in range(int(low),int(max)+1):
        for j in str(i):
            if j not in a:
                break
        else:
            l.append(i)
        
    prod()

def prod():
    for i in l:
        for j in l:
            if new_a==sorting(str(i)+str(j)):
                pr.append(int(i)*int(j))
    pr.sort()
    print(pr[-1])

def space_fixer(a):
    x=''
    for i in a:
        if i.isnumeric() and i.isspace()==False:
            x+=i
    return x
    
    

y=input("Enter number ")
if "0" in y:
    print("Cannot enter 0 ")
else:
    a=space_fixer(y)
    new_a=sorting(a)
    if len(a)>=3 and len(a)<=100:
        first_n_last(a)
    else:
        print("Number list should be the range of 3 to 100")
        


          

