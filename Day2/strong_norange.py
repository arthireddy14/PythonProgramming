def fact(n):
    f=1
    i=1
    while(i<=n):
        f=f*i
        i+=1
        
    return f

def strong_no(n):
    temp=n
    sum=0
    while(n>0):
        rem=n%10
        sum+=fact(rem)
        n=n//10
    if(temp==sum):
        print(temp,end=' ')

def display(n1):
    for i in range(1,n1+1):
        strong_no(i)

num=int(input("Enter a no. "))
print("Strong nos between 1 to ",num," are ")
display(num)
    