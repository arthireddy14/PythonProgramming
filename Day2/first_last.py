def first_last_digit(n):
    l_digit=n%10
    sum=0
    print("Last digit is ",l_digit)
    while(n>0):
        rem=n%10
        sum=sum*10+rem
        n=n//10
    
    f_digit=sum%10
    print("First digit is ",f_digit)

num=int(input("Enter a no. "))
first_last_digit(num)