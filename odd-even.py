# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain" agar dono numbers even (2 se divide hote hain) nahi toh print kare "Dono numbers even nahi hai"

def check_number(n1,n2):
    if n1%2==0 and n2%2==0:
        print("both the number are even")
    else:
        print("both the number even  nhi hai")
check_number(23,34)
