def factors(n1):
    for j in range(1,n1):
        if(n1%j==0):
            print(j,end=' ')


num=int(input("Enter a no. "))
print("Factors of ",num," are ")
factors(num)
