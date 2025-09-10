def char_count(str1,ch):
    ct=1
    for i in range(len(str1)):
        if(str1[i]==ch):
            ct+=1
    return ct

def make_str(str2,ch,ct):
    print(str2+ch+ct)
    
str1=input("Enter a string ")
for i in range(len(str1)):
    x=char_count(str1,str1[i])
    make_str()
    
    
#aaaaccbb->a4c2b2

