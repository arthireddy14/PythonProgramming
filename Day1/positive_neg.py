def positive_nega(n):
    if(n>0):
        return True
    elif(n==0):
        print("Neither postive noe negative")
        return
    else:
        return False

a=int(input())  
b=positive_nega(a)
print(b)