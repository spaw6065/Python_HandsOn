# 2. find the valid ip address from the weblog.txt.
# Validity of an ip address is that it ranges between 0 and 256 both inclusive.

f_handler = open("TextFiles/weblog.txt","r")

for x in f_handler.readlines():
    if len(x) > 1:
        ip_address = (x.split(" "))[2]
        #print("ip_address",ip_address)
        ip_address_list = str(ip_address).split(".")
        #print("ip_address_list",ip_address_list)
        for ip_addr in ip_address_list:
            #print("mod ip addr",ip_addr.replace("\n",'') )
            if int(ip_addr.replace("\n",'')) > 255:
                print("Invalid IP Address ",ip_address)
                break
    else:
        pass

