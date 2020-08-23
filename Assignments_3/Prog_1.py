# 1.Check if the password is strong enough.
# Conditions for password strength are mentioned
# below:
# Get input from user
# Password should contain special characters
# Password should contain characters
# Password length should be equals to or greater than 8
import re

def check_password(input_passwd):
    if len(input_passwd) < 8:
        return -1
    else:
        small_letter_check = re.search("[a-z]+",input_passwd)
        caps_letter_check = re.search("[A-Z]+",input_passwd)
        number_check = re.search("[0-9]+",input_passwd)
        special_char_check = re.search("[!,$@#%&*!]+", input_passwd)

        try:
            small_letter = small_letter_check.group()
            caps_letter = caps_letter_check.group()
            numbercheck = number_check.group()
            specialcharcheck = special_char_check.group()
            return 0
        except AttributeError:
            #print("AError -1")
            return -1
        return 0

def help():
    f_handler = open("TextFiles/password_help_info")
    print(f_handler.read())

if __name__ == "__main__":
    status = int()
    while True:
        inp_passwd = input("Enter the password")
        status = check_password(inp_passwd)
        #print(f"status {status}")
        if status == -1:
            print("Your password is not strong enough.")
            input_help = input("Enter the help menu for password (y/n)")
            if input_help.lower() == 'y':
                help()
            else:
                print("No password check initiated")
                break
        else:
            print("Your password is strong")
            break

