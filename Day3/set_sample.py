def additem(set1,n1):
    set1=set1.union({n1})
    return set1
    
def display(set1):
    print("Set contains ",set1)


set1=set()
while True:
    n=int(input("Enter elements to add(stop enter -1) "))
    if(n==-1):
        break
    set1=additem(set1,n)
    
display(set1)

