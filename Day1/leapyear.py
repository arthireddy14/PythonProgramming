def check_leapyr(n):
    if(n%4==0 and (n%400==0 or n%100!=0)):
      return True
    else:
        return False

x=int(input())
print(check_leapyr(x))