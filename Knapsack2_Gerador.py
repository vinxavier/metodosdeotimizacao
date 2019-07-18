from random import randint
from copy import copy

n = 120
r= 5
W=[]
P=[]
M=0

OptP = 0
OptX = []

        
def Knapsack2(l, CurW, X):
    global OptP, OptX,W,P,M
    if l==n:
        currentProfit = 0
        for i in range(n):
            currentProfit += X[i]*P[i]
        if currentProfit>OptP:
            OptP = currentProfit
            OptX = copy(X)
    else:
        if CurW + W[l]<=M:
            X[l] = 1
            Knapsack2(l+1, CurW+W[l], X)
        X[l] = 0
        Knapsack2(l+1, CurW, X)
    
        
def knapsack_uncorrelated(n,r):
    pesos, valores = [], []
    for i in range(n):
        pesos.append(randint(1,r))
        valores.append(randint(1,r))
    capacidade = sum(pesos)/1000
    capacidade = r + 1 if capacidade <= r else capacidade
    return pesos, valores, capacidade

def knapsack_weakly_correlated(n,r):
    pesos, valores = [],[]   
    for i in range(n):
        pesos.append(randint(1,r))
        valores.append(max(pesos[i]+randint(1,r/5 +1)-r,1))             
    capacidade = sum(pesos)/1000
    capacidade =  r + 1 if capacidade <= r else capacidade
    return pesos, valores, capacidade

def knapsack_strongly_correlated(n,r):
    pesos, valores = [], []
    for i in range(n):
        pesos.append(randint(1,r))
        valores.append(pesos[i]+10)
    capacidade = sum(pesos)/1000
    capacidade = r + 1 if capacidade <= r else capacidade
    return pesos, valores, capacidade        

   
   
W,P,M = knapsack_uncorrelated(n, r)

def generateX():
    X=[]
    for i in range(n):
        X.append(0)
    return X

X=generateX()
Knapsack2(0, 0, X)
print("W: ", W)
print("P: ", P)
print("M: ", M)
print("OptP: ", OptP)
print("OptX: ", OptX)