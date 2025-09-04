def palindrome_n(n):
    temp=n
    sum=0
    while(n>0):
        rem=n%10
        sum=sum*10+rem
        n=n//10
    if(temp==sum):
        print(temp,end=' ')

def display(n):
    for i in range(1,n+1):
        palindrome_n(i)


num=int(input("Enter a no. "))
print("Palindrome nos between 1 to ",num," are ")
display(num)