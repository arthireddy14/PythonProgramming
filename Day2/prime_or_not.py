def prime_not(n):
    i=2
    while(i<=(n/2)):
        if((n%i==0)):
            print("Not a prime")
            return
        i+=1
    print("Prime no.")

num=int(input("Enter a no "))
prime_not(num)