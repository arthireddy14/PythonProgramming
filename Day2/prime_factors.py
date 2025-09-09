def isprime(n1):
    i=2
    while(i<=(n1/2)):
        if((n1%i==0)):
           return False
           
        i+=1
    return True


def prime_factors(n):
    print(f"Prime factors of {n} are:")
    for i in range(2, n + 1):
        if n % i == 0 and isprime(i):
            print(i, end=" ")

num=int(input("Enter a no. "))
print("Prime factors of ",num," are ")
prime_factors(num)


