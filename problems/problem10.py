def isPrime(n):
    for i in range (2, n//2  + 1):
        if n % i == 0:
            return False
    else: 
        return True
    
sum = 5 # We are starting with 2 + 3

for i in range(4, 2_000_000):
    if isPrime(i):
        sum += i

print(sum)