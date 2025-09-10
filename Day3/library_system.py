def addbook(set1,i1,n1):
    set1[i1]=n1
    return set1
def removebook(set1,i1):
    if i1 in set1.keys():
        del set1[i1]
    else:
        print("Book not found")
def searchbook(set1,i1):
    if i1 in set1.keys():
        print("Title of book with id ",i1," is ",set1[i1])
    else:
        print("Book not found")

def updatebook(set1,i1,n1):
    if i1 in set1.keys():
        set1[i1]=n1
        print("Updated Title of book with id ",i1," is ",set1[i1])
    else:
        print("Book not found")
        
def displaybooks(set1):
    print("Dictionary is ",set1)    

def count_dict(set1):
    ct=0
    for i in set1.keys():
        ct+=1  
    return ct  
    
        


set1={}
print("1.Add book")
print("2.Remove book")
print("3.Search book")
print("4.Update book")
print("5.Display books")
print("6.Count books")
print("7.Exit")

while True:
    n=int(input("Enter the choice "))
    if(n==1):
        i1=int(input("Enter book id "))
        n1=input("Enter book name ")
        set1=addbook(set1,i1,n1)
    elif(n==2):
        i1=int(input("Enter book id to remove "))
        set1=removebook(set1,i1)
    elif(n==3):
        i1=int(input("Enter book id to search "))
        searchbook(set1,i1)
    elif(n==4):
        i1=int(input("Enter book id to update "))
        n1=input("Enter title to update ")
        updatebook(set1,i1,n1)
    elif(n==5):
        displaybooks(set1)
    elif(n==6):
        print("Count of books is ",count_dict(set1))
    elif(n==7):
        print("Exiting...")
        break
    else:
        print("Invalid choice,try again")