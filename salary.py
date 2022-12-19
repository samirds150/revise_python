from emp import *

name = input("Enter your name : ")
basic = int(input("Enter your basic salary : "))

gross = basic + ta(basic) + hra(basic)
inhand = gross - pf(basic) - pt(gross)
 


print("HRA of ", name, " is : ", hra(basic))
print("TA of ", name, " is : ", ta(basic))
print("Gross of ", name , " is : ", gross)
print("pf of ", name , " is : ", pf(basic))
print("pt of ", name , " is : ", pt(gross))
print("Inhand of ", name , " is : ", inhand)