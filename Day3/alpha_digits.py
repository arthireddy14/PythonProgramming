def digit_ct(str1):
    ct=0
    for i in str1:
        if(i>='0' and i<='9'):
            ct+=1
    return ct
def alpha_ct(str1):
    ct=0
    for i in str1:
        if('a'<=i<='z' or 'A'<=i<='Z'):
            ct+=1
    return ct

str1=input("Enter a string ")
print("Length of string ",len(str1))
print("Count of alphabets is ",alpha_ct(str1))
print("Count of digits is ",digit_ct(str1))
rem=len(str1)-alpha_ct(str1)-digit_ct(str1)
print("Count of special characters is ",rem)