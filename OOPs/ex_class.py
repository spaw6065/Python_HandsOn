class employee:
    emp_name = str()
    def get_empname(self):
        self.emp_name = input("Enter the employee name ")
        return self.emp_name

    def print_empname(self,emp_name):
        print(f"You have entered : {self.emp_name}")
        print(f"You have entered 2 : {emp_name}")

emp = employee()
emp_list = list(employee)

for x in range(0,10):
    emp_list = employee.get_empname(emp)

# for enm in emp_list:
#     employee.print_empname(enm)


# ename = emp.get_empname()
# emp.print_empname(ename)