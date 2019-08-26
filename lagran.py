from urllib.request import urlopen
from xmlrpc.client import MAXINT
from copy import copy
import random
import math
from math import ceil

def read_instance(url):
    with urlopen(url) as f:
        numbers = [int(string)
                   for line in f.readlines()
                   for string in line.split()]
    m, n = numbers[0:2]
    c = numbers[2:2+n]
    A = [[0 for j in range(n)] for i in range(m)]
    position = 2 + n
    for i in range(m):
        for k in range(numbers[position]):
            A[i][numbers[position + k]] = 1
        position += numbers[position] + 1
    b = [1 for i in range(m)]
    return m, n, c, A, b
 
m, n, c, A, b = read_instance(
    "http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/scp41.txt"
)



# Acompanhar numero de interações
loops = 0

# Definir melhor solucao encontrada para lowerBound
bestX = []

#definindo pi e lambda
pi = random.uniform(0.0001,2)
EPSON = pi/1000
lamb = []

#chutando valores iniciais de lambda
for i in range(m):
    lamb.append(random.uniform(0,0.8))

#chute inicial de Zub
Zub = 0
for custo in c:
    Zub += custo * 1
    
print("First roof: ", Zub)
    
#definir zlb
Zlb = -MAXINT

#Calculo do sub gradiante Gi
def subgradient(X, i):
    zero = None
    sum = 0
    for j in range(n):
        sum -= A[i][j]*X[j]
    if sum==0:
        zero=i   
    return 1 + sum, zero


#Calculo do escalar T
def scalar(G):
    sum = 0
    for i in range(m):
        sum += math.pow(G[i], 2)
    if sum == 0:
        return -1;
    else:
        return pi*(Zub-Zlb)/sum

#Calculo de Cj
def definingCj(j):
    sum = 0
    for i in range(m):
        sum -= lamb[i]*A[i][j]
    return c[j] + sum

#calcudo de Zub
def findZub(X, ZEROS):
    curZub = 0
    index  = 0
    for zero in ZEROS:
        minC = MAXINT
        for j in range(m):
            if X[j] == 0 and A[zero][j]!=0 and c[j]<minC:
                minC = c[j]
                index = j
        X[index] = 1
    for i in range(m):
        curZub += c[i]*X[i]    
    return curZub, X
            
        

#calculo de Zlb
def findZlb():
    tempZlb = 0
    X = []
    for j in range(n):
        X.append(0)
        Cj = definingCj(j)
        if Cj<0:
            tempZlb += Cj
            X[j] = 1
    tempZlb += sum(lamb)
    return ceil(tempZlb), X

ESTADO = 0

while(pi>EPSON):
    curZlb, curX = findZlb()
    
    G=[]
    zeros = []
    if curZlb>Zlb:
        Zlb = curZlb        
        print("New Low bound: ", Zlb)
        
    
    for i in range(m):
        g, zero = subgradient(curX, i)
        G.append(g)
        if(zero!= None):
            zeros.append(zero)
        
    curZub, curFeasibleX = findZub(curX,zeros)
    
    if curZub<Zub:
        Zub = curZub
        bestX = copy(curFeasibleX)
        print("New upper bound: ", Zub)    
        
    if (Zlb==Zub):
        ESTADO = 1
        pi = EPSON
    
    T = scalar(G)
    if T < 0:
        ESTADO = 2
        pi = EPSON
    else:
        for i in range(m):
            lamb[i] = max(0, lamb[i]+T*G[i])
    loops+=1
    pi -= EPSON
    
if ESTADO == 0:
    print("Optimal solution was not found")
    print("The optimal solution is between ", Zlb, " and ", Zub)
    print("The best feasible solution found was: ", bestX)
    print( "This solution has a value of: ", Zub)
elif ESTADO == 1:
    print("Optimal Solution has be found.")
    print("The optimal Solution is: ", bestX)   
    print( "This solution has a value of: ", Zub) 
else:
    print("The problem has found a divide by zero problem")
    print("The optimal solution is between ", Zlb, " and ", Zub)
    print("The best feasible solution found was: ", bestX)
    print( "This solution has a value of: ", Zub)


print("There was ", loops, " iterations.")
    


