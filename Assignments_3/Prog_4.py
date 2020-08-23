#4. WAP to read an entire text file.
f_handler = open("TextFiles/names.txt","r")
y = f_handler.read()
print(y)
f_handler.close()