def collatz(n): 
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0:
            n /= 2
        else: 
            n = 3*n + 1
    
    return count

maxCount = 0

for i in range(1, 1_000_001):
    print(i)
    count = collatz(i)
    if count > maxCount:
        maxCount = count
        maxCountVar = i

print(maxCountVar,":", maxCount)    