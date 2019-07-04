from ortools.linear_solver import pywraplp

MIN_NORMAL_ACCOUNTS = 100
MIN_CORPORATE_ACCOUNTS = 25

nAccounts = [6,5,4,3,6,5,4]
cAccounts = [0,1,2,3,0,1,0]
wSalary = [1200,1200,1200,1200,900,900,600]

p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = p.infinity()

x = [p.IntVar(0, infinity,str(i+1)) for i in range(7)]

p.Add(p.Sum([x[i]*nAccounts[i] for i in range(7)])>=100)
p.Add(p.Sum([x[i]*cAccounts[i] for i in range(7)])>=25)
p.Add(p.Sum([x[i] for i in range(6)])-2*x[6]>=0)

p.Minimize(p.Sum([x[i]*wSalary[i] for i in range(7)]))

p.Solve()

cpas = p.Sum([x[i].solution_value() for i in range(4)])
exp = x[4].solution_value()+x[5].solution_value()

print("Número de funcionários CPAs = ",cpas)
print("Número de funcionários Experienced = ",exp)
print("Número de funcionários Junior = ", x[6].solution_value())

print("Total de custo de operação semanal:", p.Objective().Value())