class A:
    def M1(self):
        print("M1")
    def M2(self):
        print("M2")

class B(A):
    def M3(self):
        print("M3")
    def M4(self):
        print("M4")

class C(A):
    def M5(self):
        print("M5")
    def M6(self):
        print("M6")

class D(B):
    def M7(self):
        print("M7--")
    def M81(self):
        print("M8")

class E(C):
    def M7(self):
        print("M7")
    def M8(self):
        print("M8")

class F(D,E):
    def M9(self):
        print("M9")
    def M10(self):
        print("M10")

a1  = A()

print("--GrandFather--")
a1.M1()
a1.M2()
a1.M1()
a1.M1()

print("--Father--")
b1 = B()
b1.M1()
b1.M2()
b1.M3()
b1.M4()

print("--Father--")
c1 = C()
c1.M1()
c1.M2()
c1.M5()
c1.M6()

print("--Child--")
d1 = D()
d1.M1()
d1.M2()
d1.M3()
d1.M4()
d1.M7()
d1.M81()

print("--Child--")
e1 = E()
e1.M1()
e1.M2()
e1.M5()
e1.M6()
e1.M7()
e1.M8()

print("--Grand Grand Child--")
f1 = F()
f1.M1()
f1.M2()
f1.M3()
f1.M4()
f1.M5()
f1.M6()
f1.M7()
f1.M8()
f1.M9()
f1.M10()