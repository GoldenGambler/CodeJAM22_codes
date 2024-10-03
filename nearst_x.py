x=int(input("Enter the value to raised to the power "))
n=int(input("Enter the number to which it should match "))
def looper():
    i=0
    while True:
        if ((x**i)-n)<0 and ((x**(i+1))-n)>0:
            if (((x**i)-n)*-1)>((x**(i+1))-n):
                print((x**(i)))
                break
            elif (((x**i)-n)*-1)<((x**(i+1))-n):
                print(x**(i+1))
                break
            else:
                print((x**(i)))
                break
        else:
            i+=1