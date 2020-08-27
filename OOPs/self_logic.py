# class computer:
#     def __init__(self):
#         print("inside init")
#     def config(self):
#         print("Inside config")
#
# c1 = computer()
# c1.__init__()
# c1.config()

##Program 2
class computer:
    def __init__(self,comp,RAM):
        self.comp = comp
        self.RAM = RAM
        print(f"Computer name {comp} and RAM : {RAM} GB")
    def config(self):
        print("Inside config")
        print(f"Computer name {self.comp} and RAM : {self.RAM} GB")

##Create objects
c1 = computer("MyPC",4)
#c1.__init__()
c1.config()

c2 = computer("MyPC2",8)
c2.config()


##Check object types
print(type(c1))
print(id(c1))
print(id(c2))

##Assign an object to another
c2 = c1

print(id(c1))
print(id(c2))

if c1 == c2:
    print("True")
else:
    print("False")


##