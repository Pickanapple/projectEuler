from functools import cache

@cache
def palindrome(n):
    return str(n) == str(n)[::-1]

def isLychrel(n):
    iters = 0
    n += int(str(n)[::-1])

    while True: 
        iters += 1
        if palindrome(n): 
            return False
        elif iters > 51: 
            return True
        else: n += int(str(n)[::-1])

total = 0
for i in range(10_001):
    total += isLychrel(i)

print(total)