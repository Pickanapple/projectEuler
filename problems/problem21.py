def findDivisors(n):
    divisors = []
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            if i not in divisors and i != n:
                divisors.append(i)
            if n // i not in divisors and n // i != n:
                divisors.append(n // i)

    return divisors       

def amicable(n):
    a = sum(findDivisors(n))
    b = sum(findDivisors(a))
    
    if n == b: 
        return True
    else: 
        return False
    
total = 0
for i in range(10_001):
    total += i if amicable(i) else 0

print(total)