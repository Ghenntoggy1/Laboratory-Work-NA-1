# 5. Improving algorithm
import math
import numpy as np
import sympy as sp


def BrentsMethod(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("Signs on endpoints should differ")
    if abs(f(a)) < abs(f(b)):
        c = a
        a = b
        b = c
    c = a
    flag = True
    iterations = 0
    while abs(b - a) > tol:
        fa = f(a)
        fb = f(b)
        fc = f(c)
        if fa != fc and fb != fc:
            L0 = (a * fb * fc) / ((fa - fb) * (fa - fc))
            L1 = (b * fa * fc) / ((fb - fa) * (fb - fc))
            L2 = (c * fb * fa) / ((fc - fa) * (fc - fb))
            xn = L0 + L1 + L2
        else:
            xn = b - ((fb * (b - a)) / (fb - fa))
        if ((xn < (3 * a + b) / 4) or xn > b) or (
                flag == True and (abs(xn - b)) >= (abs(b - c) / 2)) or (
                flag == False and (abs(xn - b)) >= (abs(c - d) / 2)) or (
                flag == True and (abs(b - c)) <= tol) or (
                flag == False and (abs(c - d)) < tol):
            xn = (a + b) / 2
            flag = True
        else:
            flag = False
        fxn = f(xn)
        d = c
        c = b
        if (fa * fxn) < 0:
            b = xn
        else:
            a = xn
        if abs(fa) < abs(fb):
            aux = b
            b = a
            a = aux
        iterations += 1
        if abs(b - a) < tol:
            continue
        else:
            print("Iteration:", iterations)
            print("f(Root):", f(b))
            print("Root Approximation:", b)
    return b, iterations


print("You should select such an interval [a,b] such that f(a) * f(b) < 0, i.e. should differ by sign")
x = sp.symbols('x')
f_func1 = input("Input equation (ex: 3*x**2+6*x+2): ")
f_func = sp.lambdify(x, f_func1)
lower_bound = float(input("Enter lower bound: "))
upper_bound = float(input("Enter upper bound: "))
tolerance = float(input("Enter error tolerance: "))
root, iterat = BrentsMethod(f_func, lower_bound, upper_bound, tolerance)
print("====================================")
print("Last Iteration:", iterat)
print("Root:", root)
print("f(Root):", f_func(root))
print("====================================")
