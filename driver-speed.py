# Driver speed:
def driver(speed):
    if speed<=70:
        print("ok")
    elif speed>70:
        s=speed-70
        points=s//5
        print("points:",points)
        if points>12:
            print("licence suspanded")

speed=int(input("enter the speed"))   
driver(speed)