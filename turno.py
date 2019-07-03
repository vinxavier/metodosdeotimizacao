from ortools.linear_solver import pywraplp

custos = [15,25,52,22,54,24,55,23,16]

p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = p.infinity()

n=11

s = [p.IntVar(0, infinity,"turno "+str(i+1)) for i in range(n)]

p.Add(s[0]+s[1]+s[2]>=8)
p.Add(s[1]+s[2]>=10)
p.Add(s[2]+s[3]+s[4]>=22)
p.Add(s[4]+s[5]+s[6]>=20)
p.Add(s[6]+s[7]>=16)
p.Add(s[6]+s[7]+s[8]>=8)
p.Add(s[2]+s[3]+s[4]-s[9]==0)
p.Add(s[2]+s[4]-.4*s[9]>=0)
p.Add(s[4]+s[5]+s[6]-s[10]==0)
p.Add(s[4]+s[6]-.4*s[10]>=0)
p.Add(s[2]>=2)
p.Add(s[6]>=2)


p.Minimize(p.Sum(s[k]*custos[k] for k in range(9)))

p.Solve()
for i in range(n):
    print(s[i].solution_value(),"turno", i+1)

print("soma:", p.Objective().Value())
