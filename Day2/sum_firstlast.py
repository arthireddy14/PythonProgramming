def sum_first_last(n):
    sum=n%10
    sum1=0
    while(n>0):
        rem=n%10
        sum1=sum1*10+rem
        n=n//10
    sum+=(sum1%10)
    return sum
num=int(input("Enter a no. "))
print("Sum of 1st and last digit is ",sum_first_last(num))