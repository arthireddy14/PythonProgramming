def isduplicate(l1,i):
    ct2=0
    for j in l1:
        if(j==i):
            ct2+=1
    if(ct2>1):
        return True
    else:
        return False
    
    
def count_dup(l1):
    ct=0
    checked=[]
    for i in l1:
        if(isduplicate(l1,i) and i not in checked):
            ct+=1
            checked.append(i)
    print("Count of duplicates is ",ct)
    
l1=[1,5,6,2,1,6,8,9,9]
count_dup(l1)