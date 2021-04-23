# sum and average number

def sum(a,b):
    sum=a+b
    def avg(sum):
        avg=sum/2
        return avg
    a=avg(sum)
    print("average",a)
    return sum
s=sum(4,6)
print("sum",s)
