from functools import cache

@cache
def fact(n): 
    if n <= 2: 
        return n
    else: 
        return n * fact(n - 1)

num = str(fact(100))
print(num)

total = 0
for i in num: 
    total += int(i)

print(total)