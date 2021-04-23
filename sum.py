# add_numbers naam ka function likhiye jo do numbers ko arguments ke tarah le aur fir unka sum print karta hai. Arguments ka naam number1 aur number2 hona chaiye. Input :-
def add_list():
    a=[]
    b=[]
    sum=0
    s=[]
    for i in range(0,5):
        l1=int(input("enter the number"))
        l2=int(input("enter the second number"))
        a.append(l1)
        b.append(l2)
        sum=sum+l1+l2
        s.append(sum)
    print(a)
    print(b)
    print(s)


add_list()
