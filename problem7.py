def isPrime(n):
    if n == 1:
        return False
    elif n == 2: 
        return True
    
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
        
    return True

def nthPrime(n):

    lastPrime = [2]

    for i in range(n-1):
        j = lastPrime[-1] + 1

        while not isPrime(j):
            j += 1

        lastPrime.append(j)

    return lastPrime[-1]

if __name__ == "__main__":
    print(nthPrime(10_001))