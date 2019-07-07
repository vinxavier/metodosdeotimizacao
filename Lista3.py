from random import randint

n = 0
W=[]
P=[]
M=999999999
OptP = 0
OptX = []

def Knapsack1(l, X):
    if l==n+1:
        currentWeigth = 0
        for i in range(n):
            currentWeigth += X[i]*W[i]
        if currentWeigth <= M:
            CurP = 0
            for i in range(n):
                CurP = P[i]*X[i]
            if CurP > OptP:
                OptP = CurP
                OptX = X
    else:
        X[l] = 1
        Knapsack1(l+1, X)
        X[l] = 0
        Knapsack1(l+1, X)
        
def Knapsack2(l, CurW, X):
    if l==n+1:
        currentProfit = 0
        for i in range(n):
            currentProfit += X[i]*P[i]
        if currentProfit>OptP:
            OptP = currentProfit
            OptX = X
    else:
        if CurW + W[l]<=M:
            X[l] = 1
            Knapsack2(l+1, CurW+W[l], X)
        X[l] = 0
        Knapsack2(l+1, CurW, X)
        
def Knapsack3(l,CurW,X):
    print("nothig")
    
        
def knapsack_uncorrelated(n,r):
    pesos, valores = [], []
    for i in range(n):
        pesos.append(randint(1,r))
        valores.append(randint(1,r))                
            
        
    