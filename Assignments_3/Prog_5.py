#5. WAP to read first 3 lines of a file.
f_handler=open("TextFiles/names.txt")
no_of_lines = int()
while no_of_lines <= 2:
    print(f_handler.readline())
    no_of_lines += 1