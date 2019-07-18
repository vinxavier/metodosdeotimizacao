from random import randint
from copy import copy
from urllib.request import urlopen

numero_instancia = 8 # pode ser de 1 a 8

url_base = "http://people.sc.fsu.edu/~jburkardt%20/datasets/knapsack_01"
with urlopen("{}/p0{}_w.txt".format(url_base, numero_instancia)) as arquivo:
    pesos = [int(linha) for linha in arquivo.readlines()]
with urlopen("{}/p0{}_p.txt".format(url_base, numero_instancia)) as arquivo:
    valores = [int(linha) for linha in arquivo.readlines()]
with urlopen("{}/p0{}_c.txt".format(url_base, numero_instancia)) as arquivo:
    capacidade = int(arquivo.read())
n = len(pesos)


OptP = 0
OptX = []

    
    

def GreedyRKnap(l, capacidade):
    global pesos, valores
    vxp = []
    for i in range(l, n):
        vxp.append((valores[i]/pesos[i], i))
    vxp.sort(key=None, reverse=True)
    curW = capacidade
    profit = 0
    for i in range(0, len(vxp)):
        index = vxp[i][1]
        if pesos[index]<=curW:
            profit += valores[index]
            curW -= pesos[index]
        else:           
            return profit + (curW/pesos[index])*valores[index]
    return profit
       
def Knapsack3(l, CurW, X):
    global OptP, OptX,pesos,valores,capacidade
    currentProfit = 0
    for i in range(n):
        currentProfit += X[i]*valores[i]
    if l==n:        
        if currentProfit>OptP:
            OptP = currentProfit
            OptX = copy(X)
    else:
        B = currentProfit + GreedyRKnap(l, capacidade-CurW)
        if OptP<=B:
            if CurW + pesos[l]<=capacidade:            
                X[l] = 1
                Knapsack3(l+1, CurW+pesos[l], X)
        if OptP<=B:
            X[l] = 0
            Knapsack3(l+1, CurW, X)
        
        

def generateX():
    X=[]
    for i in range(n):
        X.append(0)
    return X

X=generateX()
Knapsack3(0, 0, X)

print("pesos: ", pesos)
print("valores: ", valores)
print("Capacidade: ", capacidade)
print("OptP: ", OptP)
print("OptX: ", OptX)