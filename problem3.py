def isPrime(n):
    if n == 1:
        return False
    elif n == 2: 
        return True
    
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
        
    return True

def primeFactorise(n: int) -> str:
    factors = []
    if isPrime(n): 
        factors.append(n)
        return factors
    
    if n == 4:
        return [2, 2]

    for i in range(2, (n//2)):
        if n%i == 0:
            factors.append(i)
            factors.append(int(n/i))

    for i in factors: 
        if not isPrime(i):
            factors.remove(i)
            factors.extend(primeFactorise(i))

    return factors

# for i in range(4, 10):
#     print(f"{i}: {factorise(i)}")

if __name__ == "__main__":
    print(primeFactorise(12))
    print(sum(primeFactorise(12)))