from random import randint
from copy import copy
from urllib.request import urlopen

numero_instancia = 7 # pode ser de 1 a 8

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

def Knapsack1(l, X):
    global OptP, OptX,pesos,valores,capacidade
    if l==n:
        currentWeigth = 0
        for i in range(n):
            currentWeigth += X[i]*pesos[i]
        
        if currentWeigth <= capacidade:
            CurP = 0
            for i in range(n):
                CurP += valores[i]*X[i]
            if CurP > OptP:
                OptP = CurP
                OptX = copy(X)
    else:
        X[l] = 1
        Knapsack1(l+1, X)
        X[l] = 0
        Knapsack1(l+1, X)
        
def Knapsack2(l, CurW, X):
    global OptP, OptX,pesos,valores,capacidade
    if l==n:
        currentProfit = 0
        for i in range(n):
            currentProfit += X[i]*valores[i]
        if currentProfit>OptP:
            OptP = currentProfit
            OptX = copy(X)
    else:
        if CurW + pesos[l]<=capacidade:
            X[l] = 1
            Knapsack2(l+1, CurW+pesos[l], X)
        X[l] = 0
        Knapsack2(l+1, CurW, X)
        

def generateX():
    X=[]
    for i in range(n):
        X.append(0)
    return X

X=generateX()
Knapsack1(0, X)

print("pesos: ", pesos)
print("valores: ", valores)
print("Capacidade: ", capacidade)
print("OptP: ", OptP)
print("OptX: ", OptX)