from functools import cache

@cache
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

i = 0

while True: 
    if len(str(fib(i))) >= 1000:
        print(i)
        quit()
    else: 
        i += 1
