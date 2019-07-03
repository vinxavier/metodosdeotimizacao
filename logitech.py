from ortools.linear_solver import pywraplp

MAX_CUSTO = 100000
MAX_MANUTENCAO = 50000
MAX_VEICULOS = 8

custos = [26000, 30000, 24000, 32000, 50000, 60000]
capacidade = [7,8,9,11,20,24]
manutencao = [5000, 3500, 6000, 8000, 7000, 110000]
labels = ["Nissan Van", "Toyota Van", "Plymouth Van", "Ford(Stretch) Van",
          "Mitsubishi Minibus","General Motors Minibus"]

p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = p.infinity()

x = [p.IntVar(0, infinity, labels[i]) for i in range(6)]

p.Add(p.Sum([x[i]*custos[i] for i in range(6)])<=MAX_CUSTO)
p.Add(p.Sum([x[i]*manutencao[i] for i in range(6)])<=MAX_MANUTENCAO)
p.Add(p.Sum([x[i] for i in range(6)])<=MAX_VEICULOS)
p.Add(x[4]+x[5]>=1)
p.Add(x[0]+x[1]+x[2]+x[3]>=3)
p.Add(x[2]+x[3]+x[5] - 0.5 * p.Sum([x[i] for i in range(6)])>=0)

p.Maximize(p.Sum([x[i]*capacidade[i] for i in range(6)]))

p.Solve()
for i in range(6):
    print("Número de ", x[i]," = ",x[i].solution_value())

print("Total de assentos:", p.Objective().Value())
