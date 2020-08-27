import math
class school:
    school = "ethans"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def marks_avg(self):
        avg = (self.m1+self.m2+self.m3)/3
        return self.m1+self.m2+self.m3,avg

    @classmethod
    def get_schoolname(self,cls):
        self.m1 = 100
        print("marks 1",self.m1)
        print(cls.school)

    @staticmethod
    def get_school():
        m1 = 30
        print("marks 1",m1)
        print(school)

if __name__ == "__main__":
    s1 = school(10,20,30)
    sum,average = s1.marks_avg()
    print(f"Grand Total :{sum} | Average : {average}")
    s1.get_schoolname(cls=s1)
    s1.get_school()

    print("------------")
    s2 = school(40,50,60)
    sum2,average2 = s2.marks_avg()
    print(f"Grand Total :{sum2} | Average : {average2}")
    s2.get_schoolname(cls=s2)
    s2.get_school()
    #school.get_school(cls=s1)