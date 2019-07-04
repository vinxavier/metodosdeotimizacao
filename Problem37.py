from ortools.linear_solver import pywraplp

#Required Production
REQ_PRODUCTION = 100000

labels = ["Springfield","Oak Ridge", "Westchester"]

#Changeover Cost
cCustos = [1200,1100,1000]
#Transportation Cost
tCustos = [224,280,245]
#Produção Máxima de cada fábrica
maxP = [65000, 50000, 55000]

p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = p.infinity()

x = [p.IntVar(0, infinity,labels[i]) for i in range(3)]
b = [p.BoolVar(labels[i]+" produziu") for i in range(3)]

for i in range(3):
    p.Add(x[i]<=maxP[i]*b[i])

p.Add(p.Sum([x[i] for i in range(3)])==REQ_PRODUCTION)

p.Minimize(p.Sum([b[i]*cCustos[i]+x[i]*tCustos[i]/1000 for i in range(3)]))

p.Solve()

for i in range(3):
    print("Número de peças fabricadas em", x[i]," = ",x[i].solution_value())
    if(b[i].solution_value()):
        print(b[i])

print("Custo total: ", p.Objective().Value())