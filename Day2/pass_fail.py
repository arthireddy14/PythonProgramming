def checkpf(m):
    if(m>=40):
        if(m<=50):
            print("Grade C")
        elif(m>50 and m<=70):
            print("Grade B")
        elif(m>70 and m<=80):
            print("Grade A")
        elif(m>80 and m<=100):
            print("Destinction")
    else:
        print("Fail")


sname=input()
srno=int(input())
marks1=int(input("Enter sub marks1 "))
marks2=int(input("Enter sub marks2 "))
marks3=int(input("Enter sub marks3 "))
checkpf(marks1)
checkpf(marks2)
checkpf(marks3)
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

