l=[37,46,22,40,8,37,44,43,50,45]
a=82
l.sort()
l.reverse()
l1=[]

def add():
    for i in l:
        if (sum(l1)+i)<=a:
            l1.append(i)
            if sum(l1)==a:
                break
    print(l1)
add()