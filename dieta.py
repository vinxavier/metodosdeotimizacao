from ortools.linear_solver import pywraplp

dieta = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

x1 = dieta.IntVar(0, 4, "frango")
x2 = dieta.IntVar(0, 3, "ovos")
x3 = dieta.IntVar(0, 8, "feijao")
x4 = dieta.IntVar(0, 2, "leite")
x5 = dieta.IntVar(0, 2, "peixe")

dieta.Add(205 * x1 + 160 * x2 + 140 * x3 + 300 * x4 + 150 * x5 >= 2000)
dieta.Add(32  * x1 + 15  * x2 + 8   * x3 + 15  * x4 + 37  * x5 >= 60)
dieta.Add(12  * x1 + 50  * x2 + 240 * x3 + 100 * x4 + 150 * x5 >= 900)

dieta.Minimize(30 * x1 + 10 * x2 + 20 * x3 + 40 * x4 + 50 * x5)

dieta.Solve()
for var in [x1, x2, x3, x4, x5]:
    print(var.name(), "=", var.solution_value())
print("Custo total:", dieta.Objective().Value())