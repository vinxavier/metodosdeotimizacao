from ortools.linear_solver import pywraplp

MAX_AD = 250
BUDGET = 1000000

labels = ["Television","Radio", "Newspaper"]

#custo de cada ad
custos = [4000,500,1000]
#custo de produção de ad para determinada mídia
pCustos = [500000,50000,100000]
alcance = [500000, 50000, 200000]

p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = p.infinity()

x = [p.IntVar(0, infinity,labels[i]) for i in range(3)]
b = [p.BoolVar(labels[i]+" produziu") for i in range(3)]

for i in range(3):
    p.Add(x[i]<=MAX_AD*b[i])

p.Add(p.Sum([x[i]*custos[i]+b[i]*pCustos[i] for i in range(3)])<=BUDGET)

p.Maximize(p.Sum([x[i]*alcance[i] for i in range(3)]))

p.Solve()

for i in range(3):
    print("Número de ADs em ", x[i]," = ",x[i].solution_value())
    if(b[i].solution_value()):
        print(b[i])

print("Total de espectadores alcançados: ", p.Objective().Value())