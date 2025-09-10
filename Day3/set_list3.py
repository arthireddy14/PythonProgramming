

l1=[1,5,3,7,8,2]
l2=[3,6,2,8,1,4,6,2]
l3=[8,5,2,4,1,9,0]
set1=set(l1)
set2=set(l2)
set3=set(l3)
set4=set1.union(set2)
set5=set4.union(set3)
print("Total number of attendees ",len(set5))
set6=set1.symmetric_difference(set2)
set7=set2.symmetric_difference(set3)
set8=set6.symmetric_difference(set7)
print(set8)
print("Exactly one day attended count is ",len(set8))
print("day1 and day2 attendees ",set1.intersection(set2))
print("day2 and day3 attendees ",set2.intersection(set3))
print("day1 and day3 attendees ",set1.intersection(set3))