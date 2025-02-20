from functools import cache

@cache
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

total = 0
#I just kept adding 9s
for i in range(3, 99999): 
    tempTotal = 0
    for j in str(i): 
        tempTotal += fact(int(j))
        if tempTotal == i:
            total += i

print(total)