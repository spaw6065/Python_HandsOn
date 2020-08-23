#6. WAP to append text to a file and display the text.
import os
f_handler=open("TextFiles/names.txt","a+")

text = input("Enter the text")
f_handler.write("\n")
f_handler.write(text)

f_handler.close()

r_handler = open("TextFiles/names.txt","r")
# print(len(r_handler.read())+1)
# print(len(text))
r_handler.seek(0,os.SEEK_END) ##goes to the end of file
r_handler.seek(r_handler.tell() - len(text))
print(r_handler.read())
