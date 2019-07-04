from ortools.linear_solver import pywraplp

MAX_AD = 250
MIN_ALCANCE = 30000000

labels = ["Television","Radio", "Newspaper"]
custos = [4000,500,1000]
alcance = [500000, 50000, 200000]

p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = p.infinity()

x = [p.IntVar(0, infinity,labels[i]) for i in range(3)]

for i in range(3):
    p.Add(x[i]<=MAX_AD)

p.Add(p.Sum([x[i]*alcance[i] for i in range(3)])>=MIN_ALCANCE)

p.Minimize(p.Sum([x[i]*custos[i] for i in range(3)]))

p.Solve()

for i in range(3):
    print("Número de ADs em ", x[i]," = ",x[i].solution_value())

print("Menor Custo com Marketing: ", p.Objective().Value())