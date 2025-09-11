#exception handling
num=int(input("Enter a number "))
deno=int(input("Enter another number "))
try:
    x=(num/deno)
    # print(x)
except:
    print("Error: division by 0 not supported" )
else:
    print(x)
finally:
    print("Always executes")