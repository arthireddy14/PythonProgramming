def concate_2(str1,str2):
    str3=""
    for i in str1:
        str3+=i
       
    for i in str2:
        str3+=i
        
def comp_str12(str1,str2):
    if(len_str(str1)!=len_str(str2)):
        print("Strings are not equal")
    i=0
    ct=len_str(str1)
    while i<ct:
        if(str1[i]!=str2):
            print("String are not equal")
        i+=1
    print("String are equal")
    
        
def len_str(str1):
    ct=0
    for i in str1:
        ct+=1
    print("Length of string ",str1," is ",ct)

str1=input("Enter a string1 ")
len_str(str1)
str2=input("Enter string2 ")
len_str(str2)
comp_str12(str1,str2)
print("Concate of two strings ",concate_2(str1,str2))