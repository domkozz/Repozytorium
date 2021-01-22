import math

print("Wzór równania kwadratowego y = ax^2+bx+c")
a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
c=float(input("Podaj c: "))
delta=(b*b)-4*(a*c)

pierwDelty=math.sqrt(delta)
x1=((-b)-pierwDelty)/(2*a)
x2=((-b)+pierwDelty)/(2*a)

print("Delta jest równa= ", delta)
print("X1 jest równe= ",x1)
print("X2 jest równe= ",x2)
