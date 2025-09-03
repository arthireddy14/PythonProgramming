cno=input()
cname=input()
pmr=int(input())
lmr=int(input())
tot_units=pmr-lmr
cost_perunit=3.80
cur_bill=tot_units*cost_perunit
print("Consumer no ",cno)
print("Consumer name ",cname)
print("Present month reading ",pmr)
print("Last month reading ",lmr)
print("Total units ",tot_units,"   Current bill amt ",cur_bill)
print(f"Consumer no {cno}, Consumer name {cname}, Present month reading {pmr}")