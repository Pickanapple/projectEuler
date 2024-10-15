primes = [2, 3, 5, 7]

# #if any(t < 0 for t in x

# def isPrime(n):
#     if any(i < n//2 for i in primes):
#         if n % i == 0:
#             return False
    
#     primes.append(i)
#     return True
    
# sum = 17

# list = [i for i in range(9, 2_000_000, 2)]
# print(list)

# for i in list:
#     print(f"{i}: {sum}")
#     print(primes)
#     if isPrime(i):
#         sum += i

# print(sum)

def isPrime(n):
    if n in primes:
        return True

    if n == 2:
        return True
    
    if n < 2:
        return False
    
    for i in primes:
        if i > n or i == primes[-1]:
            primes.append(n)
            return True
        elif n % i == 0:
            return False
        

for i in range (1000):
    if  isPrime(i):
        print(i)