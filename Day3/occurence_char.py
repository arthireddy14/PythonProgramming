def occurence_char(str1,c):
    l1=[]
    for i in range(len(str1)):
        if(str1[i]==c):
            l1.append(i)
    return l1
str1=input("Enter a string ")
ch=input("Enter a character to search ")
if(ch not in str1):
    print(ch," not present in string")
else:
    print(occurence_char(str1,ch))
    print("Count of occurence of ",ch," is ",len(occurence_char(str1,ch)))