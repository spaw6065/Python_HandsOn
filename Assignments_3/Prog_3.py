# 3. from Names.txt, extract the first name and last name and then store it in another file which
# has the format <first name> <second name>

f_handler = open("TextFiles/names.txt","r")
w_handler = open("TextFiles/names_output.txt","w+")
while True:
    y = f_handler.readline()
    if y != '':
        print("------------------")
        fname,lname = y.split(",")
        w_handler.write(fname+lname)
    else:
        break
f_handler.close()
w_handler.close()


