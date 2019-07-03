from ortools.linear_solver import pywraplp

NUM_FABRICAS = 4
NUM_TIPOS_VEICULOS = 3

custos = [[15, 20, 40, 150],
          [15, 28, 29, 170],
          [10, 24, 50, 125],
          [14, 15, 25, 500]]

cotas = [30,20,10]


problema = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = problema.infinity()

#Variáveis
f = [[problema.IntVar(0, infinity, ("Produção na fábrica " + str(j+1) +" do veículo " + 
                                    str(i+1))) for i in range(NUM_TIPOS_VEICULOS)] 
                                    for j in range(NUM_FABRICAS)]

p = [problema.BoolVar("Fabrica "+str(j+1)) for j in range(NUM_FABRICAS)]


#Restrições
for i in range(NUM_TIPOS_VEICULOS):
    problema.Add(problema.Sum([f[j][i] for j in range(NUM_FABRICAS)])==cotas[i])
    
for j in range(NUM_FABRICAS):
    problema.Add(problema.Sum([f[j][i] for i in range(NUM_TIPOS_VEICULOS)])<=p[j]*60)
    
#Objetivo
problema.Minimize(problema.Sum([f[j][i]*custos[j][i] for i in range(NUM_TIPOS_VEICULOS) 
                                for j in range(NUM_FABRICAS)])+ 
                                problema.Sum([p[j]*custos[j][3] for j in range(NUM_FABRICAS)]))


problema.Solve()

for j in range(NUM_FABRICAS):   
    for i in range(NUM_TIPOS_VEICULOS):
        print(f[j][i].name(), " = ", f[j][i].solution_value())
print("Custo total:", problema.Objective().Value())