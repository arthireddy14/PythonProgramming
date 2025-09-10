def delete_element(l1,pos):
    if(pos>len(l1)):
        print("Position not found")
    else:
        i=pos
        while(i<=len(l1)-1):
            l1[i]=l1[i+1]
            i+=1
        print("List is")
        for i in range(0,len(l1)-1):
            print(i,end=" ")
        
l1=[]
while True:
    n=int(input("Enter elements in list(stop enter -1) "))
    if(n==-1):
        break
    l1.append(n)

x=int(input("Enter position to delete element "))
delete_element(l1,x)