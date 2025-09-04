def print_val(n1):
    if(n1==1):
        print("One",end=" ")
    elif(n1==2):
        print("Two",end=" ")
    elif(n1==3):
        print("Three",end=" ")
    elif(n1==4):
        print("Four",end=" ")
    elif(n1==5):
        print("Five",end=" ")
    elif(n1==6):
        print("Six",end=" ")
    elif(n1==7):
        print("Seven",end=" ")
    elif(n1==8):
        print("Eight",end=" ")
    elif(n1==9):
        print("Nine",end=" ")
    else:
        print("Zero",end=" ")

def revers(n):
    sum=0
    while(n>0):
        rem=n%10
        sum=sum*10+rem
        n=n//10
    return sum


def no_to_word(n):
    n=revers(n)
    while(n>0):
        rem=n%10
        print_val(rem)
        n=n//10

num=int(input("Enter a no. "))
print("Words of no is ")
no_to_word(num)

