from urllib.request import urlopen

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

pi = 1
lamb = []

Zub = 0

for i in range(m):
    lamb.append(1)

def subgradient(bi, Ai, Xi):
    sum = 0
    for j in range(n):
        sum = Ai[j]*Xi[j]
    return bi - sum

def scalar(G, Zub, Zlb):
    sum = 0.0
    for i in range(m):
        sum = G[i]**2
    return pi*(Zub-Zlb)/sum

