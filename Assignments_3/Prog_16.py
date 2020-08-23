# 16.
# get a file name from user through command line:
# if file is available in the directory
# check if the size of file is > 1 KB
# check if the file extension is .txt
# check the creation date of the file
# create a backup of this file:file_name_bkup_10Jun2020
import os
import datetime as dt
filename = input("Enter the filename")
datepart = dt.date.today()
modified_datepart = str(datepart).replace("-","_")
print("date part",modified_datepart)

bkp_filename = filename+"_bkup"+modified_datepart
print("backup filename ",bkp_filename)

if os.path.isfile(filename):
    if os.stat(filename).st_size > 1:
        if filename.endswith(".txt"):
            #get the file creation date

            print("creation date",os.stat(filename).st_ctime)
            print(dt.datetime.fromtimestamp(os.stat(filename).st_ctime).strftime('%c'))

            f_handler = open(filename,"r")
            w_handler = open(bkp_filename,"w")
            for x in f_handler.read():
                w_handler.write(x)
        else:
            print("File extension is not .txt")
    else:
        print("File size is less than 1 KB")
else:
    print("File doesnot exists")

