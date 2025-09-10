def addElement(list1,n1):
    list1.append(n1)
    # for i in list1:
    #     print(i,end=" ")
    print(list1)


list1=[]
while True:
    n=int(input("\nEnter element to add into list(stop enter -1) "))
    if(n==-1):
        break
    addElement(list1,n)