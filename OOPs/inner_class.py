class students:
    school_name = "Ethans"
    def __init__(self,name,roll):
        self.name= name
        self.roll = roll

    def show(self):
        print(f"name : {self.name} rollno : {self.roll}")
        self.lap = self.laptop(self)

    class laptop:
        def __init__(self,cls2):
            self.brand = "HP"
        def show(self,cls2):
            print(f"values ",cls2.name)
            print(f"values ", cls2.roll)
            print(f"values ", cls2.school_name)
            print(f"laptop : {self.brand}")

s1 = students("Ajay",99)
s1.show()

lap1 = s1.laptop(cls2=s1)
lap1.show(cls2=s1)

s2 = students("Vijay",19)
s2.show()

lap2 = s2.laptop(cls2=s1)
lap2.show(cls2=s2)


