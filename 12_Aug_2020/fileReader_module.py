from yield_in_python import file_reader as fr

def init():
    file_Name="dataset_2"
    dir_loc = "C:\\Users\\SPA702\\Datasets\\"
    file_loc_name=dir_loc+file_Name
    return file_loc_name

file_loc_name = init()
print("File Name ",file_loc_name)
ldict = fr.run(file_loc_name)
fr.print2(dictionary=ldict)
