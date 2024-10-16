#Source: https://en.wikipedia.org/wiki/Lattice_path for the binomial part

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

def binomial(a, b):
    return fact(a)/(fact(b)*fact(a-b))

def latticePath(a, b):
    return binomial(a + b, a)

print(latticePath(20, 20))