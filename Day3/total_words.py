def count_words(str1):
    
    if(len(str1)<0):
        return 0
    else:
        ct=1
        for i in range(len(str1)):
            if(str1[i]==" "):
                ct+=1
        return ct

str1=input("Enter a string ")
print("Count of words in string ",count_words(str1))