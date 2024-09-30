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

    i = 2

    while i not in factors and i + 1 not in factors:
        if n%i == 0:
            factors.append(i)
            factors.append(int(n/i))
            break

        i += 1

    for i in factors: 
        if not isPrime(i):
            factors.remove(i)
            factors.extend(primeFactorise(i))

    return factors

# for i in range(4, 10):
#     print(f"{i}: {factorise(i)}")

if __name__ == "__main__":
    print(primeFactorise(600851475143))
    print(max(primeFactorise(600851475143)))