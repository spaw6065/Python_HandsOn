##String operations
# str1=input("Enter the string")
# print("string is ",str1)
# print("Cap string is ",str1.capitalize())
#
# print("Captialise each word",str1.title())

##case fold
str1 = "WELCOME TO "
str2 = "Ethans"

print((str1 + str2).casefold())

print((str1 + str2).center(50,"*"))

newStr=(str1 + str2).center(50,"*")
print("length of string",len(newStr))

print(newStr.translate("Ethans"))

character=input("Enter the character")
print(newStr.count(character))

print(newStr.istitle())
newStr.replace("Ethans","Baner")
print("Partition ",newStr.partition(" "))
print(newStr)

print("Split",type(newStr.split(" ")))

pyVersion = 3.0
newStr2 = "Welcome to Python"+str(pyVersion)
print(newStr2.endswith("3.0"))

newStr3 = "hello worlds"
print(newStr3.find("world"))

print(newStr3.ljust(50,"*"))
print(newStr3.rjust(50,"|"))
print((newStr3.rjust(50)).ljust(50))
print(newStr3.center(50))

newStr="hurrah! we won the match"
print(type(newStr.split(" ")))
print(type(newStr.partition(" ")))

newStr4 = "My name is Sumit"
newStr4_enc = newStr4.encode()
print(newStr4.encode())

newStr4_dec = newStr4_enc.decode()
print(newStr4_dec)

newStr5 = "Welcome To Ethans"
newStr5_replace = newStr5.replace("Welcome","welCOME")
print(newStr5_replace)



print('{4:2f}'.format(29))
print("sumit".title())

##join
newStr6 = "Hell"
joinChr = "o"
joinStr = "World"
joinedStr = newStr6.join(joinChr)
print(joinedStr)
print(newStr6.join(joinStr))





