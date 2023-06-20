# Ex 1. Bisection Method
import math
from prettytable import PrettyTable


def function(var):
    return math.exp(var) - math.pow(var, 2)


def BisectionMethod(ai, bi, tol, iterations=0):
    error = 1
    while abs(error) >= tol:
        iterations += 1
        n_vals.append(iterations)
        c = (bi+ai)/2
        c_vals.append(c)
        func_vals.append(function(c))
        error = bi - c
        error_vals.append(error)
        if function(a) * function(c) < 0:
            a_vals.append(ai)
            b_vals.append(bi)
            bi = c
        else:
            a_vals.append(ai)
            b_vals.append(bi)
            ai = c


error_tol = math.pow(10, -8)
a = -2
b = 0
n_vals = []
a_vals = []
b_vals = []
c_vals = []
func_vals = []
error_vals = []
BisectionMethod(a, b, error_tol)

x = PrettyTable()
x.add_column("n", n_vals)
x.add_column("a", a_vals)
x.add_column("b", b_vals)
x.add_column("c", c_vals)
x.add_column("f(c)", func_vals)
x.add_column("error", error_vals)
print(x)
print(f"Root: {c_vals[-1]}")
print(f"Value of function in this root: {function(c_vals[-1])}")
