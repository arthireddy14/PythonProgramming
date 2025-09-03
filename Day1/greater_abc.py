def greater(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c
        
x=int(input())
y=int(input())
z=int(input())
print("Grater value is ",greater(x,y,z))