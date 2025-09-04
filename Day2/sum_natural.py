def sum_natural(n):
    i=1
    sum=0
    while(i<=n):
        sum+=i
        i+=1
    return sum

num=int(input("Enter a number "))
print("Sum of natural nos is ",sum_natural(num))