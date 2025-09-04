def perfect_no(n):
    temp=n
    sum=0
    for j in range(1,(n//2)+1):
        if(n%j==0):
            sum+=j
    
    if(sum==temp):
        print(temp,end=' ')

def display(n1):
    for i in range(1,n1+1):
        perfect_no(i)


num=int(input())
print("Perfect nos between 1 to ",num," are ")
display(num)