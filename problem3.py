def isPrime(n):
    if n == 1:
        return False
    elif n == 2: 
        return True
    
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
        
    return True

def factorise(n):
    factors = []
    if isPrime(n): 
        factors.append(n)
        return factors
    
    for i in range(2, n//2):
        if n%i == 0:
            factors.append(i)
            factors.append(int(n/i))

    for i in factors: 
        if not isPrime(i):
            factors.append(i for i in factorise(i))

    return factors

for i in range(1, 10):
    print(f"{i}: {factorise(i)}")