def alpha_check(c):
    if('a'<=c<='z' or 'A'<=c<='Z'):
        print("Alphabet")
    elif(c>='0' and c<='9'):
        print("Digit")
    else:
        print("Special character")

c=input()
alpha_check(c)