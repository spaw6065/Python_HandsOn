import os

def count_lines_in_file(file_abs_path):
    cntr = 1
    f_handler = open(file_abs_path,"r")
    for x in f_handler.read():
        if x == "\n":
            cntr += 1
        else:
            pass
    f_handler.close()
    return cntr

#7. WAP to read last n lines of a file.
def read_last_x_lines(file_abs_path):
    f_handler = open(file_abs_path, "r")
    for line in f_handler.readlines():
        #print(line)
        pass

#8. WAP that takes a text file as input and returns the number of words of a given text file.
def get_word_count(file_abs_path):
    words = list()
    tot_words = int()
    f_handler = open(file_abs_path,"r")
    for x in f_handler.readlines():
        words = (x.split(" "))
        tot_words += len(words)
    f_handler.close()
    return(tot_words)

#10. WAP to copy the contents of a file to another file.
def copy_file_contents(oldfilename,
                       abs_path_new_path,
                       newfile):
    #Check if directory exists or not and if not exists then create and copy the files.
    if os.path.isdir(abs_path_new_path):
        if os.path.isfile(abs_path_new_path+"/"+newfile) == False:
            f_handler = open(oldfilename,"r")

            w_handler = open(abs_path_new_path+"/"+newfile,"a+")
            for line in f_handler.readlines():
                w_handler.write(line)

            f_handler.close()
            w_handler.close()
    else:
        os.mkdir(abs_path_new_path)
        if os.path.isfile(abs_path_new_path+"/"+newfile) == False:
            f_handler = open(oldfilename,"r")

            w_handler = open(abs_path_new_path+"/"+newfile,"a+")
            for line in f_handler.readlines():
                w_handler.write(line)

            f_handler.close()
            w_handler.close()

#11. WAP to get the file size of a plain file.
def get_file_size(filename):
    return os.stat(filename).st_size

#12. WAP to find the longest word from a file.
def max_len_word(filename):
    words = list()
    gt_len_word = int()
    gt_word = str()

    #f_handler = open(filename,"r")
    with open(filename,'r') as f_handler:
        for x in f_handler.readlines():
            words = x.split(" ")
            #print("words ",words)
            for y in words:
                #print(f"y |{y}|")
                if gt_len_word <= len(y):
                    gt_len_word = len(y)
                    gt_word = y
                    #print("gt_len_word ",gt_len_word)
                    #print("gt_word ", gt_word)
    return(gt_len_word,gt_word)

##Main method starts from here
if __name__=="__main__":
    filepath = "TextFiles"
    abs_path_new_file = "C:/Users/SPA702/PycharmProjects/21_July_2020/Assignments_3/CopyFiles"

    for filename in os.listdir(filepath):
        abs_file_path = filepath+"/"+filename
        #print("abs_file_path",abs_file_path)
        total_lines_in_file = count_lines_in_file(abs_file_path)

        #num_of_lines_to_read = int(input("Enter the number of lines to read from the end"))
        #read_last_x_lines(abs_file_path)

        total_words = get_word_count(abs_file_path)

        copy_file_contents(abs_file_path,
                           abs_path_new_file,
                           "copy_"+filename)
        #print(f"{filename} copied to {abs_path_new_file}/copy_{filename}")

        file_size = get_file_size(abs_file_path)

        gt_len_word,gt_word = max_len_word(abs_file_path)

        print(f"file : {filename} |  location : {filepath} | lines : {total_lines_in_file} | words : {total_words} | size :{file_size} | max length word : {gt_word} | length max word : {gt_len_word}.")
