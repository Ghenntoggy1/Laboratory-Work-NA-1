# Ex 3. Muller's Method
import math
from prettytable import PrettyTable


def f(x):
    return math.pow(x, 3) + 2*math.pow(x, 2) + 10*x - 20


def MullersMethod(tol):
    error = 1
    i = 2
    while abs(error) > tol:
        h1 = x_vals[i-1] - x_vals[i-2]
        h2 = x_vals[i] - x_vals[i-1]
        delta1 = (f(x_vals[i-1]) - f(x_vals[i-2])) / h1
        delta2 = (f(x_vals[i]) - f(x_vals[i-1])) / h2
        d = (delta2 - delta1) / (h2 + h1)
        b = delta2 + h2*d
        dlt = math.sqrt(math.pow(b, 2) - 4*f(x_vals[i])*d)
        if abs(b-dlt) < abs(b+dlt):
            e = b + dlt
        else:
            e = b - dlt
        error = (-2*f(x_vals[i]))/e
        error_vals.append(error)
        p = x_vals[i] + error
        x_vals.append(p)
        i += 1


p0 = 0
p1 = 1
p2 = 2
err_tol = math.pow(10, -8)
x_vals = [p0, p1, p2]
error_vals = []
MullersMethod(err_tol)
# print(x_vals)
# print(error_vals)
iters = [i for i in range(1, len(x_vals) + 1)]
x = PrettyTable()
x.field_names = ['n', 'x', 'error']
for i in range(len(x_vals)):
    if i < 3:
        x.add_row([iters[i], x_vals[i], "-"])
    else:
        x.add_row([iters[i], x_vals[i], error_vals[i-3]])

print(x)