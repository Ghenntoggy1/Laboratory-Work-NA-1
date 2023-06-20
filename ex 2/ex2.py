# Ex 2. Interesting function
import math
import numpy as np

def f(x, c1):
    return 1*x - c1*math.pow(x, 2)


def df(x, c1):
    return 1 - 2*c1*x


def Newton_method(c1, epsilon, x0):
    xn = x0
    for j in range(1, 1001):
        fxn = f(xn, c1)
        dfxn = df(xn, c1)
        xn1 = xn - fxn / dfxn
        if abs(1/c1 - xn) < epsilon:
            print("====================================================")
            print("Iteration: ", j, f"\t at c = {c1}", "\t Found Limit =", xn1)
            print("====================================================")
            break
        else:
            print("Iteration: ", j, "\t Approximation =", xn1)
        xn = xn1


xi0 = 3
tolerance = 0.000001
c = 2
Newton_method(c, tolerance, xi0)



# # Sa intreb de 2/c sau 1/c !!!

# # 2. Interesting function
# import math
# import numpy as np
#
#
# def f(x, c1):
#     return 2 * x - c1 * x**2
#
#
# def Fixed_Point(c1, init_guess, tol):
#     x_old = init_guess
#     x_new = f(x_old, c1)
#     iterations = 100
#     iteration = 0
#     while abs(x_new - x_old) > tol and iteration < iterations:
#         x_old = x_new
#         x_new = f(x_old, c1)
#         iteration += 1
#     return x_new
#
#
# c = int(input("Input c: "))
# initial_guess = 0.5
# tolerance = float(input('Input error tolerance: '))
#
#
# limit = Fixed_Point(c, initial_guess, tolerance)
# print(f"The limit of the fixed-point iteration is: {limit}")
#