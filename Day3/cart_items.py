def display(l1):
    print("Your cart is ",l1)

def additem(l1,n):
    l1.append(n)
    print("Your cart is ",l1)
    return l1

def searchitem(l1,n):
    if n in l1:
        print("Found item ",n)
    else:
        print("Not Found item ",n)

def removeitem(l1,x):
    if(x not in l1):
        print("Item ",x," not present in list")
        return l1
    else:
        newl1=[]
        for i in l1:
            if(i!=x):
                newl1=newl1+[i]
        print("New list is ",newl1)
        return newl1
        

l1=[]
print("1.Add element to cart")
print("2.Remove element in cart")
print("3.Search element in cart")
print("4.Display list")
print("5.Total elements in cart")
print("6.Sort the list")
print("7.Clear list")
print("8.Exit")
while True:
    n=int(input("Enter a choice "))
    if(n==1):
        x=input("Enter element to add ")
        l1=additem(l1,x)
    elif(n==2):
        x=input("Enter element to remove ")
        l1=removeitem(l1,x)
    elif(n==3):
        x=input("Enter element to search ")
        searchitem(l1,x)
    elif(n==4):
        display(l1)
    elif(n==5):
        print("Total count of elements ",len(l1))
    elif(n==6):
        print("Exiting...")
        break
    else:
        print("Invalid choice,try again")
        
    