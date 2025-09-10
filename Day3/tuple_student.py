def highest_marks(l1):
    max1=l1[0][2]
    name=l1[0][1]
    for i in l1:
        if(i[2]>max1):
            max1=i[2]
            name=i[1]       
    print("Highest marks student name is ",name)
    
def grater_75(l1):
    for i in l1:
        if(i[2]>75):
            print(i[1],"->",i[2],end=" ")



l1=[]
tup1=(123,"ANANYA",80)
tup2=(124,"Raju",76)
tup3=(125,"Manu",90)
tup4=(126,"Manu1",60)
tup5=(127,"Manu2",70)

l1.append(tup1)
l1.append(tup2)
l1.append(tup3)
l1.append(tup4)
l1.append(tup5)
highest_marks(l1)
print("Marks greater than 75 ")
grater_75(l1)
