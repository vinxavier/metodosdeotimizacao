# -*- coding: utf-8 -*-
from ortools.linear_solver import pywraplp

NEW_TRUCKS = 5000
MIN_AMERICAN_TRUCKS = 3000
MAX_MONTHLY = 2750000
MIN_CAPACITY = 10000

labels = ["Ford","Chevrolet","Dodge","Mack","Nissan","Toyota"]
mLease = [500,600,300,900,200,400]
cOutlay = [2000,1000,5000,9000,2000,0]
capacity = [1000, 1000, 750, 5000, 500, 750]

p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = p.infinity()

x = [p.IntVar(0, infinity,labels[i]) for i in range(6)]

p.Add(p.Sum([x[i] for i in range(6)])==5000)
p.Add(p.Sum([x[i] for i in range(4)])>=3000)
p.Add(p.Sum([x[i]*mLease[i] for i in range(6)])<=2750000)
p.Add(p.Sum([x[i]*capacity[i] for i in range(6)])>=10000000)

p.Minimize(p.Sum([x[i]*cOutlay[i] for i in range(6)]))

p.Solve()

for i in range(6):
    print(x[i], ": ", x[i].solution_value())
print(p.Objective().Value())
