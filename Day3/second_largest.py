def second_largest(l1):
    max1=l1[0]
    max2=0
    for i in l1:
        if (i>max1):
            max2=max1
            max1=i
            
    print("Second largest is ",max2)
    
    
l1=[]
while True:
    n=int(input("Enter list elements (stop enter -1) "))
    if(n==-1):
        break
    l1.append(n)
    
    
second_largest(l1)    
