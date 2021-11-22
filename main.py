import time
print("degrés ?")
d = int(input("Degrés = "))
if d == 2:
    print("On a les racines :")
    X1 = int(input("x1 = "))
    X2 = int(input("x2 = "))

    print("On a aussi un point de coordonées :")
    x = int(input("x = "))
    y = int(input("y = "))

    ax = (x - X1) * (x - X2)
    a = y / ax

    xs = (X1 + X2) / 2
    ys = a * (xs - X1) * (xs - X2)

    print("f(x)=a(x-x1)(x-x2)")
    print("avec a =", a)
    print("avec un sommet S(", xs, ";", ys, ")")

if d == 3:
    nr = int(input("nombres de racine"))
    if nr == 1:
        b = int(input("b = "))

        x = int(input("x = "))
        y = int(input("y = "))

        ax = y - b

        x3 = x * x * x

        a = ax / x3

        print("f(x)=ax3+b")
        print("avec a =", a)

    if nr > 1:
        print("On a les racines :")
        x1 = int(input("x1 = "))
        x2 = int(input("x2 = "))
        x3 = int(input("x3 = "))

        print("On a aussi un point de coordonées :")
        x = int(input("x = "))
        y = int(input("y = "))

        ax = (x - x1) * (x - x3) * (x - x3)
        a = y / ax

        xs = (x1 + x2) / 2
        ys = (xs - x1) * (xs - x3) * (xs - x3)

        print("f(x)=a(x-x1)(x-x2)(x-x3)")
        print("avec a =", a)
        print("avec un sommet S(", xs, ";", ys, ")")

time.sleep(3)