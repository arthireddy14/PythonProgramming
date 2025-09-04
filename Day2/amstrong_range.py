def amstrong(n):
    temp1=n
    ct=0
    while(n>0):
        rem=n%10
        ct+=1
    sum=0
    temp=temp1
    while(n>0):
        rem=n%10
        sum+=rem*rem*rem
        n=n//10
    if(temp==sum):
        print(temp,end=' ')

def display(n1):
    for i in range(1,temp1+1):
        amstrong(i)

n1=int(input("Enter a no. "))
print("Amstrong no. between 1 to ",n1," are")
display(n1)