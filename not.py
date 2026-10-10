salary=float(input())
g=input()
if g=="m":
    bonus=0.05*salary
elif g=="f":
    bonus=0.10*salary
else:
    bonus=0
#comdition for extra bonus 
if salary<10000:
    bonus=bonus+0.02*salary  #extra 2%
total_salary=salary+bonus
print(f"{bonus:.2f}")
print(f"{total_salary:.2f}")