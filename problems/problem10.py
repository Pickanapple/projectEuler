primes = [2, 3, 5, 7]

#if any(t < 0 for t in x

def isPrime(n):
    if any(i < n//2 for i in primes):
        if n % i == 0:
            return False
    
    primes.append(i)
    return True
    
sum = 17

list = [i for i in range(9, 2_000_000, 2)]
print(list)

for i in list:
    print(f"{i}: {sum}")
    print(primes)
    if isPrime(i):
        sum += i

print(sum)