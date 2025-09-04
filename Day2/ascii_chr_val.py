def ascii_char():
    for i in range(48,123):
        print(i,"-",chr(i),end=" ")

print("Printing all ascii values and their characters")
ascii_char()