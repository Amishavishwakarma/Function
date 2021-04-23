
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



def list_change(a,b):
    h=[]
    for i in range(0,len(a)):
        h.append(calculator(a[i],b[i],"multiplication"))
    print(h)
