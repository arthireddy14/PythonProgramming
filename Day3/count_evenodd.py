def count_even(l1):
    print("List is ",l1)
    ct1=0
    ct2=0
    for i in l1:
        if(i%2==0):
            ct1+=1
        else:
            ct2+=1
    print("Count of even no.s in list ",ct1)
    print("Count of odd no.s in list ",ct2)
    

l1=[]
while True:
    n=int(input("Enter list elements to add(stop enter -1) "))
    if(n==-1):
        break
    l1.append(n)

count_even(l1)
