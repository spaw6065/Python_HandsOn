##Read the config file and create a dictionary for the
## english to dev nagari characters.
#Config file contents :TextFiles/English_To_DevNagari_Config
# R=\u0930
# A=\u0906
# M=\u092E
# S=\u0938
# U=\u0941
# I=\u093F
# T=\u0924
# D=\u0927
# H=\u0939

def prepare_config(config_file_name):
    dict_static_config = dict()
    with open(config_file_name,"r") as r_handler:
        for line in r_handler.readlines():
            #print("line",line)
            key = line.split("=")[0]
            #print("key ",key)
            value = line.split("=")[1]
            #print("value",value)
            dict_static_config[key]=value.replace("\n",'')
    print(dict_static_config)
    # dict123 = {'R': '\u0930', 'A': '\u0906', 'M': '\u092E', 'S': '\u0938', 'U': '\u0941', 'I': '\u093F', 'T': '\u0924',
    #            'D': '\u0927', 'H': '\u0939'}
    #
    # return dict123
    return dict_static_config


##convert the english character to devnagari character
def convert_char_eng_to_hing(cdict,char):
    return cdict[char]

def clean_up_string(dev_str):
    ##Rule 1: convert am to proper name
    print("dev_str : ",dev_str)
    final_Str = dev_str.replace('0906', '093E')

    ##Rule 2 : ....
    return final_Str

##Boiler's plate
if __name__=="__main__":
    inp_name_list = list()
    devnagari_name_str = str()
    quote_fmt = '\"'
    single_quote_fmt = '\''

    config_dict = prepare_config("TextFiles/English_To_DevNagari_Config")

    #print(config_dict)
    inp_name = input("Enter the name")

    for chr in inp_name:
        devnagari_name_str += convert_char_eng_to_hing(config_dict,chr)
        fmt_devnagari_name_str = quote_fmt + devnagari_name_str + quote_fmt


    devnagari_name = clean_up_string(fmt_devnagari_name_str)
    final_string  = devnagari_name
    print("final_string",final_string)

##print devnagari version
name=u"\u0938\u0941\u092E\u093F\u0924"
print(name)

