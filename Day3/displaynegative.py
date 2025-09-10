def displaynegative(l1):
    print("Only displaying negative no.s in list ")
    for i in l1:
        if(i<0):
            print(i,end=" ")

def addElement1(l1,n1):
    l1.append(n1)
    
    print("List is ",l1)
    displaynegative(l1)

l1=[]
while True:
    num=int(input("\nEnter elements to add to list(stop enter -1) "))
    if(num==-1):
        break
    addElement1(l1,num)
    

