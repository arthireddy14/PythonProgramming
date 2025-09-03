sname=input()
srno=int(input())
marks1=int(input("Enter sub marks1 "))
marks2=int(input("Enter sub marks2 "))
marks3=int(input("Enter sub marks3 "))
tot=marks1+marks2+marks3
avg_marks=tot/3
print("Student details")
print("Student name ",sname)
print("Student Rollno ",srno)
print("Marks of sub1 ",marks1)
print("Marks of sub2 ",marks2)
print("Marks of sub3 ",marks3)
print("Total marks of 3 subjects is ",tot)
print("Average is ",round(avg_marks,2))

