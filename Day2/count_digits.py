def count_digits(n):
    ct=0
    while(n>0):
        rem=n%10
        ct+=1
        n=n//10
       
    return ct

num=int(input("Enter a no. "))
print("Count of digits in it ",count_digits(num))
