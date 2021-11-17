import time

print("On a les racines :")
X1 = int(input("x1 = "))
X2 = int(input("x2 = "))

print("On a aussi un point de coordonées :")
x = int(input("x = "))
y = int(input("y = "))

ax = (x - X1)*(x - X2)

a = y / ax

xs = (X1 + X2)/2
ys = a*(xs - X1)*(xs - X2)

print("f(x)=a(x-x1)(x-x2)")
print("avec a =", a)
print("avec un sommet S(", xs, ";", ys, ")")
time.sleep(20)
