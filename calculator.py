# CALCULATION
def calculator(x,y,operator):
    if operator=="addition":
        num=x+y
        return num
    if operator=="multiplication":
        num1=x*y
        return num1
    if operator=="subtraction":
        num2=x-y
        return num2
    if operator=="division":
        num3=x/y
        return num3

x=int(input("enter the 1st number"))
y=int(input("enter the 2nd number"))
num=calculator(x,y,"addition")
print(num)
num1=calculator(x,y,"multiplication")
print(num1)
num2=calculator(x,y,"subtraction")
print(num2)
num3=calculator(x,y,"division")
print(3)