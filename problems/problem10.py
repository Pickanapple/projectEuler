primes = [2, 3, 5, 7]

def isPrime(n):
    if n in primes:
        return True

    if n == 2:
        return True
    
    if n < 2:
        return False
    
    for i in primes:
        
        if n % i == 0:
            return False
        elif i == primes[-1]:
            primes.append(n)
            return True
    
sum = 17

list = [i for i in range(9, 2_000_000, 2)]

for i in list:
    #print(f"{i}: {sum}")
    if isPrime(i):
        sum += i

print(sum)