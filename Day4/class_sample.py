class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("Name is ",self.name)
        print("Roll no is ",self.rollno)
        print("Marks are ",self.marks)

stu1=Student("Ananya",2389,80)
stu1.display()
stu2=Student("Chinni",2345,90)
stu2.display()