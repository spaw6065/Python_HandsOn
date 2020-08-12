def init():
    file_Name="dataset_1"
    dir_loc = "C:\\Users\\SPA702\\Datasets\\"
    file_loc_name=dir_loc+file_Name
    return file_loc_name

def run(filelocname):
    i_dict = dict()
    for filename in open(filelocname):
        # dict[filename.split(" ")(0)]=filename.split(" ")(1)
        # print("filename ", filename)
        # print("key ", (filename.rsplit("	"))[0])
        # print("value ", (filename.rsplit("	"))[1])
        key = (filename.rsplit(" "))[0]
        value = (filename.rsplit(" "))[1]
        i_dict[key] = value
        # print("----------------------")
    return i_dict

def print2(dictionary):
    for x in dictionary.items():
        print(f"{x[0]}----->{x[1]}")

if __name__ == "__main__":
    print("In main")

    file_loc_name = init()
    print("FileName ",file_loc_name)
    l_dict = run(file_loc_name)
    print2(l_dict)

    # for x in l_dict.items():
    #     print(x)
    print("Exit main")