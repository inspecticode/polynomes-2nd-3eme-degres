import time

print("On a les racines :")
x1 = int(input("x1 = "))
x2 = int(input("x2 = "))
x3 = int(input("x3 = "))

print("On a aussi un point de coordonées :")
x = int(input("x = "))
y = int(input("y = "))

ax = (x - x1)*(x - x3)*(x - x3)
a = y / ax

xs = (x1 + x2) / 2
ys =  (xs - x1)*(xs - x3)*(xs - x3)

print("f(x)=a(x-x1)(x-x2)(x-x3)")
print("avec a =", a)
print("avec un sommet S(", xs, ";", ys, ")")
time.sleep(20)
