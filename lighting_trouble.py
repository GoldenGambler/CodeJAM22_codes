lamp_list=[]
grid=[]

def accept():
    while len(lamp_list)!=m:
        print("Round",len(lamp_list)+1)
        a=eval(input("Enter coordinate of lamps used in a tuple form "))
        if a[0]<=n and a[1]<=n:
            lamp_list.append(a)
        else:
            print("Coordinate can not be bigger than grid dimension ")
    making_loop()

def making_loop():
    for i in range(n):
        temp=[]
        while len(temp)!=n:
            temp.append(0)
        grid.append(temp)
    marking_area()
    
def marking_area():
    for i in lamp_list:
        for j in range(n):
            grid[i[0]-1][j]=1
            grid[j][i[1]-1]=1
    counting_empty()
            
def counting_empty():
    c=0
    for i in grid:
        for j in i:
            if j==0:
                c+=1
    print(c)
    

n=int(input("Enter square grid dimension "))
if n>=2 and n<=100:
    m=int(input("Enter the number of lamps used "))
    if m>=1 and m<=5000 and m<=(n*n):
        accept()
    else:
        print("should be in the range of 1 to 5000")
else:
    print("n value should be the limit of 2 to 100")


            
