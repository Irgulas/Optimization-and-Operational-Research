## Importation
from ortools.linear_solver import pywraplp


##Function
def LinearProgramming():

    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    # Variable
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')

    print('Number of variables =', solver.NumVariables())

    nb_const = int(input("How many constraints ? "))
    for i in range (nb_const) :
        x1= int(input("Coeff x1 = "))
        x2= int(input("Coeff x2 = "))
        w = int(input("If >= press 0, else press 1 \n"))
        z = int(input("Result of the constraint = "))
        if w == 0 :
            solver.Add(x1 * x + x2 * y >= z)
        else :
            solver.Add(x1 * x + x2 * y <= z)

    print('Number of constraints =', solver.NumConstraints())

    a = int(input("Coeff x1 of the objective function = "))
    b = int(input("Coeff x2 of the objective function = "))

    # Objective function: 3x + y.
    max = int(input("If you whant to maximize press 1, if you whant to minimize press 2 : \n"))
    if max == 1 :
        solver.Maximize(a * x +  b * y)
    else :
        solver.Minimize(a * x +  b * y)

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        if max == 1 :
            print('Maximum =', solver.Objective().Value())
        else :
            print('Minimum =', solver.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')



