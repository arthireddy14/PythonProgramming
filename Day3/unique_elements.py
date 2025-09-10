# def addelement(l1,n):
#     i=len(l1)
#     i+=1
#     l1[i]=n
    

def unique_ele(l1):
    l2=[]
    for i in l1:
        if(i not in l2):
            l2.append(i)
            # addelement(l2,i)
    
    print("List of unique elements is ",l2)
    
    
l1=[1,5,6,2,1,6,8,4]
print("List is ",l1)
unique_ele(l1)
