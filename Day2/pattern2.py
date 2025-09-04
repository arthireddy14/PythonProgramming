def pattern_2(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(i==j or i+j==6):
                print("$",end=' ')
            else:
                print("*",end=' ')
        print()

n1=int(input())
n2=int(input())
pattern_2(n1,n2)