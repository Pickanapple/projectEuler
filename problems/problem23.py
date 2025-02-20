from functools import cache

@cache
def divisors(n): 
    divisors = set()
    divisors.add(1)

    for i in range(2, int(n**(1/2)) + 2):
        if n % i == 0: 
            if n//i not in divisors:
                divisors.add(n//i)
            if i not in divisors:
                divisors.add(i)

    return divisors

@cache
def isAbundant(n): 
    if sum(divisors(n)) > n:
        return True
    
    return False

def checkSum(nums, target):
    for i in nums: 
        for j in nums:
            if i + j == target:
                return True
            
    return False

abundants = []
total = 0

for i in range(1, 28124):
    # if i % 100 == 0:
    #     print(i)
        
    if isAbundant(i):
        abundants.append(i)
    else:
        total += i if not checkSum(abundants, i) else 0

print(total)