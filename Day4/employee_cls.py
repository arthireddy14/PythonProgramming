class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def display(self):
        print("Name is ",self.name)
        print("Salary is ",self.sal)
        
class Manager(Employee):
    def __init__(self,name,sal,dept):
        super().__init__(name,sal)
        self.dept=dept
    def display(self):
        print("Name is ",self.name)
        print("Salary is ",self.sal)
        print("Department is ",self.dept)
        
emp1=Employee("Raju",15000)
emp1.display()
mng1=Manager("Divya",20000,"Finance")
mng1.display()
        