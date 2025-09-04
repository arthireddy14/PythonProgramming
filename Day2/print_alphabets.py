def print_alphabet():
    i=1
    n='A'
    while(i<=26):
        print(n ,end=' ')
        #n=str(int(n)+1)
        n=chr(ord(n)+1)
        i+=1

print("Printing A to Z")
print_alphabet()