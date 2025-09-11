from employee_cls import Employee
class Manager(Employee):
    def __init__(self,name,sal,dept):
        super().__init__(name,sal)
        self.dept=dept
    def display(self):
        print("Name is ",self.name)
        print("Salary is ",self.sal)
        print("Deapartment is ",self.dept)
        
mng1=Manager("Divya",20000,"Finance")
mng1.display()
