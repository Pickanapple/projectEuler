from functools import cache

@cache
def sumDivisors(n): 
    divisors = set()
    divisors.add(1)

    for i in range(2, int(n**(1/2)) + 2):
        if n % i == 0: 
            if n//i not in divisors:
                divisors.add(n//i)
            if i not in divisors:
                divisors.add(i)
    
    return sum(divisors)

def amicable(n): 
    if sumDivisors(sumDivisors(n)) == n:
        return True
    else: 
        return False

total = 0
foundPairs = set()

for i in range(1, int(1E4)):
    if amicable(i):
        otherNum = sumDivisors(i)
        if otherNum < 1E4:
            if otherNum not in foundPairs and i not in foundPairs:
                foundPairs.add(i)
                foundPairs.add(otherNum)

                total += (i + otherNum)

print(total)