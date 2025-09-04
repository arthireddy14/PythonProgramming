def fact_cal(n):
    f=1
    i=1
    while(i<=n):
        f=f*i
        i+=1
    return f

num=int(input("Enter a number "))
print("Factorial of no is ",fact_cal(num))