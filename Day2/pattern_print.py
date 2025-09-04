# def pattern_print(n,m):
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             print("*",end=' ')
#         print()



def pattern_print1(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==j:
                print("$",end=' ')
            else:
                print("*",end=' ')
        print()


n1=int(input())
n2=int(input())
pattern_print1(n1,n2)


