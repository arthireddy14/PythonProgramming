def count_freq(l1,ele):
    ct=0
    for i in l1:
        if(i==ele):
            ct+=1
    print("Frequency of ",ele," is ",ct)
    
l1=[]
while True:
    n=int(input("Enter elements in list(enter -1 to stop) "))
    if(n==-1):
        break
    l1.append(n)
print("List is ",l1)
for i in l1:
    count_freq(l1,i)