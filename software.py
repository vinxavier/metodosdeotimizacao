from ortools.linear_solver import pywraplp

NUM_WORKERS = 60
MAX_CUSTO = 3500000
MAX_PRODUCTION = 3

custos = [400000, 1100000, 940000, 760000, 1260000, 1800000]
rProg = [6,18,20,16,28,34]
profit = [2000000, 3600000, 4000000, 3000000, 4400000, 6200000]

p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

x = [p.BoolVar("Aplicação: "+str(i+1)) for i in range(6)]
b = p.BoolVar("b")


p.Add(p.Sum([x[i]*rProg[i] for i in range(6)])<=NUM_WORKERS)
p.Add(p.Sum([x[i]*custos[i] for i in range(6)])<=MAX_CUSTO)
p.Add(x[3]+x[4] == b*2)
p.Add(x[1]-x[0]<=0)
p.Add(x[2]+x[5]<=1)
p.Add(p.Sum([x[i] for i in range(6)])<=MAX_PRODUCTION)

p.Maximize(p.Sum([x[i]*profit[i] for i in range(6)]))

p.Solve()

for i in range(6):
    if x[i].solution_value():
        print("A aplicação ",x[i], " será fabricada")
        
print("Solução: ", p.Objective().Value())