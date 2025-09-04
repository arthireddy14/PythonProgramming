num=int(input("Enter week no. "))
def week_check(n):
    if(n==1):
        print("Sunday")
    elif(n==2):
        print("Monday")
    elif(n==3):
        print("Tuesday")
    elif(n==4):
        print("Wednesday")
    elif(n==5):
        print("Thrusday")
    elif(n==6):
        print("Friday")
    elif(n==7):
        print("Saturday")
    else:
        print("Invalid choice")

week_check(num)


