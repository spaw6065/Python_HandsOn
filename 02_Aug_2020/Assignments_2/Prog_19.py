str = input("Enter the string ")
substr = input("Enter the substring to be searched for ")

if str.count(substr) >= 1:
    print("1 String '{}' contains substring {}".format(str,substr))
else:
    print("Substr {} not present in string '{}'".format(substr,str))