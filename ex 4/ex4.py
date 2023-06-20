# Ex 4. Nonlinear equations
import numpy as np
import sympy as sp


def parse_expression(expr_string):
    expr = sp.parse_expr(expr_string)
    return expr


def newton_raphson_system(guess, equations, tolerance):
    num_equations = len(equations)
    num_variables = len(guess)
    iteration = 0
    while True:
        iteration += 1
        f = np.zeros(num_equations)
        J = np.zeros((num_equations, num_variables))
        for i in range(num_equations):
            f[i] = equations[i](*guess)
            for j in range(num_variables):
                h = 1e-6
                x_plus_h = guess.copy()
                x_plus_h[j] += h
                J[i][j] = (equations[i](*x_plus_h) - f[i]) / h
        delta_x = np.linalg.lstsq(J, -f, rcond=None)[0]
        guess += delta_x
        if np.linalg.norm(delta_x) < tolerance:
            break

    print(f"Converged in {iteration} iterations.")
    return guess


vars = int(input("Input number of variables: "))
vars_list = []
for variable in range(vars):
    vars_list.append(sp.symbols(input(f"Input variable {variable + 1}: ")))
vars_lst = tuple(vars_list)
eq_num = int(input("Input number of equations: "))
print("Input example: x1**2+sin(x2)+exp(x3)+0*x4+x5")
equat_list = []
for equation in range(eq_num):
    equat_list.append(parse_expression(input(f"Input equation {equation + 1}: ")))

equat_list_fin = []
for i in equat_list:
    equat_list_fin.append(sp.lambdify(vars_lst, i))

initial_guess1 = []
for i in range(vars):
    initial_guess1.append(float(input(f"Input initial guess for {vars_list[i]}: ")))
initial_guess = np.array(initial_guess1, dtype=np.float64)

tolerance = float(input("Input error tolerance: "))

roots = newton_raphson_system(initial_guess, equat_list_fin, tolerance)

print("Roots:")
for i, root in enumerate(roots):
    print(f"{vars_list[i]} =", root)
