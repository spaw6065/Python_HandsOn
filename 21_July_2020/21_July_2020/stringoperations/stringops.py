str1 = "Today is tuesday.We have sprint planning at {}"
str2 = str1.format(10)
print("First String",str1)
print("Second String",str2)

print(str2.find("a",3))
print(str2.replace("10","11"))
print(str2)
print(str2.index("a"))
print(str2.center(100))
print(str2.count("a"))
print(str2.encode())

for x in range(2,30,3):
  print(x)