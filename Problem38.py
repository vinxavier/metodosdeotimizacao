# -*- coding: utf-8 -*-
from ortools.linear_solver import pywraplp

WANTED_PROFIT = 250
MAX_TCS = 750
VALOR_TCS = 55

p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = p.infinity()

tcs = p.IntVar(0,infinity,"Número de ações da TCS") 
mfi = p.IntVar(0,infinity,"Valor investido no MFI")

p.Add((tcs*13 + mfi*.09)<=WANTED_PROFIT)
p.Add(0.6*VALOR_TCS*tcs - 0.4*mfi<=0)
p.Add(tcs*VALOR_TCS<=MAX_TCS)

p.Maximize(tcs*13 + mfi*.09)

p.Solve()

print(tcs, ": ", tcs.solution_value())
print(mfi, ": ", mfi.solution_value())
