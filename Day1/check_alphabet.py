def check_alphabets(ch):
    if('a'<=ch<='z' or 'A'<=ch<='Z'):
        return True
    else:
        return False

chr=input()
print(check_alphabets(chr))