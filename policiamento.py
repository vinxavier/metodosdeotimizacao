from ortools.linear_solver import pywraplp

A=[[1,1,0,0,0,0,0,0,1,1,1,0,0,0,0],
   [1,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
   [0,1,1,1,0,0,0,1,1,0,0,0,0,0,0],
   [0,0,1,1,1,1,0,1,0,0,0,0,0,0,0],
   [0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
   [0,0,0,1,1,1,1,1,0,0,0,0,0,0,0],
   [0,0,0,0,1,1,1,1,0,0,0,0,1,1,1],
   [0,0,1,1,0,1,1,1,1,0,0,0,1,0,0],
   [1,1,1,0,0,0,0,1,1,1,0,0,1,0,0],
   [1,0,0,0,0,0,0,0,1,1,1,1,1,0,0],
   [1,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
   [0,0,0,0,0,0,0,0,0,1,1,1,1,1,0],
   [0,0,0,0,0,0,1,1,1,1,0,1,1,1,0],
   [0,0,0,0,0,0,1,0,0,0,0,1,1,1,1],
   [0,0,0,0,0,0,1,0,0,0,0,0,0,1,1]]

p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)


x=[p.BoolVar("x"+str(i+1)) for i in range(15)]

for i in range(15):
    p.Add(p.Sum([A[i][j]*x[j] for j in range(15)])>=1)

p.Minimize(p.Sum([x[j] for j in range(15)]))

p.Solve()

for i in range(15):
    if x[i].solution_value():
        print("Tem viatura na região ",i+1)
        
print("Solução: ", p.Objective().Value())
    