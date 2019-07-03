from ortools.linear_solver import pywraplp

profit = [40000,50000,60000,80000]
lot_size = [.2,.27,.22,.35]
labels = ["Tropic","Sea Breeze","Orleans", "Grand Key"]


p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = p.infinity()

#variaveis
x = [p.IntVar(0, infinity,"Model "+labels[i]) for i in range(4)]

#variavel item c
has12 = [p.BoolVar("Model "+labels[i]+" Tem Mais de 12 casas") for i in range(4)]

#restrições
p.Add(x[0]+x[1]>=40)
p.Add(x[1]+x[2]+x[3]>=50)
for i in range(4):
    p.Add(x[i]>=10)
p.Add(p.Sum([x[i]*lot_size[i] for i in range(4)])<=20)

#restrição item c
p.Add(p.Sum([has12[i] for i in range(4)])>=3)
for i in range(4):
    p.Add(x[i]>=12*has12[i])

#objetivo
p.Maximize(p.Sum([x[i]*profit[i] for i in range(4)]))

p.Solve()

for i in range(4):
    print(x[i], "=", x[i].solution_value())
print("Total profit: ", p.Objective().Value())