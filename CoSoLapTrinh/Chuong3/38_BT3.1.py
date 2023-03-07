a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
p=(a+b+c)/2
import math
dientich=math.sqrt((p*(p-a)*(p-b)*(p-c)))
if (a+b)>c and (a+c)>b and (b+c)>a:
    dientich=print("Dien tich=",round(dientich,3))
else: print("Khong hop le ")