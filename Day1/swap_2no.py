a=int(input())
b=int(input())
print("Before swapping a=",a," b=",b)
temp=a
a=b
b=temp
print("After swapping a=",a," b=",b)
print("Swapping without temp variable")
a,b=b,a
print("After swapping a=",a," b=",b)
