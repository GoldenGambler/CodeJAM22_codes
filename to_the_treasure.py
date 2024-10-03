n=int(input("Enter the grid size "))
l=[]
def fact(a):
    some_num=1
    for i in range(1,a+1):
        some_num*=i
    return some_num

def the_real():
    for i in range(n+1):
        l.append(fact(2*(n)-i)/((fact(n-i)**2)*fact(i)))
    print((sum(l)))
the_real()