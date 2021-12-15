import time

def seconDegres (x,y):
    print("On a les racines :")
    X1 = int(input("x1 = "))
    X2 = int(input("x2 = "))

    ax = (x - X1) * (x - X2)
    a = y / ax

    xs = (X1 + X2) / 2
    ys = a * (xs - X1) * (xs - X2)

    print("f(x)=a(x-x1)(x-x2)")
    print("avec a =", a)
    print("avec un sommet S(", xs, ";", ys, ")")

def troisiemeDegres (x,y):
    print("combien a t'on de racines ?")
    nr = int(input("nombres de racine = "))
    if nr == 1:
        b = int(input("b = "))

        ax = y - b

        x3 = x ** 3

        a = ax / x3

        print("f(x)=ax3+b")
        print("avec a =", a)

    if nr > 1:
        print("On a les racines :")
        x1 = int(input("x1 = "))
        x2 = int(input("x2 = "))
        x3 = int(input("x3 = "))

        ax = (x - x1) * (x - x2) * (x - x3)
        a = y / ax

        xs = (x1 + x2) / 2
        ys = (xs - x1) * (xs - x3) * (xs - x3)

        print("f(x)=a(x-x1)(x-x2)(x-x3)")
        print("avec a =", a)
        print("avec un sommet S(", xs, ";", ys, ")")

print("second ou troisième degrés ?")
d = int(input("degrés = "))

print("On a un point de coordonées :")
x = int(input("x = "))
y = int(input("y = "))

if d == 2:
    seconDegres(x,y)
    
if d == 3:
    troisiemeDegres(x,y)
    
else:
    print("degrés non compatible")
    time.sleep(5)
    exit()

time.sleep(3)
