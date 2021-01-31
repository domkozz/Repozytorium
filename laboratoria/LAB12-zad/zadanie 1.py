from cmath import sqrt


def suma(a,b):
    a=float(input("Podaj a: "))
    b=float(input("Podaj b: "))
    suma=a+b
    return suma

def roznica(a,b):
    a=float(input("Podaj a: "))
    b=float(input("Podaj b: "))
    roznica=a-b
    return roznica

def iloczyn(a,b):
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    iloczyn = a * b
    return iloczyn

def iloraz(a,b):
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    iloraz = a / b
    return iloraz

def pierwiastek(a):
    a = float(input("Podaj a: "))
    b = sqrt(a)
    return b

