def lowsorter(x):
    t=list(x)
    t.sort()
    return "".join(t)

def Mode(a):
    sample=''
    for i in range(65,97+26):
        if chr(i) not in "[\]^`_^":
            if chr(i) in a:
                sample+=chr(i)
    return sample

def accept():
    print("Type 1 to test in no case sensitivty ")
    print("Type 2 to test in case sensitivity ")
    a=input("Chose ")
    x=Mode(part1)
    y=Mode(part2)
    if a=="1":
        if lowsorter(x.lower())==lowsorter(y.lower()):
            print("true")
        else:
            print("false")
    elif a=="2":
        if x==y:
            print("true")
        else:
            print("false")
            
        
def IamDoing():
    global part1
    global part2
    while True:
        a=input("Enter a multi string ").strip()
        if len(a)>=10 and len(a)<=100:
            index=None
            for i in range(len(a)):
                if a[i].isspace():
                    index=i

            if index!=None:
                part1=a[:index].strip()
                part2=a[index:].strip()
                if part1.isalpha() and part2.isalpha():
                    for i in part2:
                        if i.isspace():
                            print("Why extra space ")
                    else:
                        accept()
                else:
                    print("Give Proper String bro")
            else:
                print("Give Proper String bro")
        else:
            print("string size not correct")
            
IamDoing()