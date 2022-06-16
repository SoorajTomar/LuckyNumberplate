import math
plate=input("Enter Number Plate:")
n=int(input('Enter Lucky Number:'))
x=int(plate[len(plate)-4:])
x1=x%9
if(x1==0): x1=9
print(n==x1)
