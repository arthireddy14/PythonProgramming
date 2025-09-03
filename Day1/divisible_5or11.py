def divisible_5_11(num):
    if(num%5==0 and num%11==0):
        return True
    else:
        return False
    
print(divisible_5_11(55))