from ortools.linear_solver import pywraplp

MAX_RESTANTES = 6
MAX_FSPACE_OCUPADO = 600
MAX_CUSTO_RESTOK = 75000

labels = ["Notebook Toshiba", "Notebook Compaq", "PC Compaq", "PC Packard Bell",
          "MacIntosh Apple", "Monitor Packard Bell", "Monitor Sony",
          "Printer Apple", "Printer HP", "Printer Epson"]
liquidation = [10000,8000,20000,12000,25000,4000,15000,5000,18000,6000]
cRestok = [15000,12000,25000,22000,20000,12000,13000,14000,25000,10000]
fSpace = [50,60,200,200,145,85,50,100,150,125]

p = pywraplp.Solver("", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

x = [p.BoolVar(labels[i]) for i in range(10)]
compaq = p.BoolVar("compaq")
packard = p.BoolVar("packard")
apple = p.BoolVar("apple")
toshiba_epson = p.BoolVar("toshiba ou epson")

p.Add(p.Sum([x[i] for i in range(10)])<=MAX_RESTANTES)
p.Add(p.Sum([x[i]*fSpace[i] for i in range(10)])<=MAX_FSPACE_OCUPADO)
p.Add(x[1]+x[2]==2*compaq)
p.Add(x[3]+x[5]==packard*2)
p.Add(x[4]+x[7]==apple*2)
p.Add(x[0]+x[9]==toshiba_epson*2)
p.Add(p.Sum([x[i] for i in range(5)])>=2)
p.Add(x[5]+x[6]>=1)
p.Add(x[7]+x[8]+x[9]>=1)
p.Add(p.Sum([x[i]*cRestok[i] for i in range(10)])<=MAX_CUSTO_RESTOK)

p.Minimize(p.Sum([x[i]*(cRestok[i]-liquidation[i]) for i in range(10)]))

p.Solve()

for i in range(10):
    if x[i].solution_value():
        print("O produto ",x[i], " vai ficar")
        
print("Solução: ", p.Objective().Value())


