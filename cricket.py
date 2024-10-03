t=int(input("Put number of test cases "))
l=[]
for i in range(t):
    l.append(int(input("Enter the number of teams ")))
    
for i in l:
    if i%2==0:
        print((i*5)//2)
    else:
        print(((i-1)*5)//2)