def fibonaci(n):
    if n < 2: 
        return n

    return round(((((1+(5)**(1/2))/2)**n) - (((1-(5)**(1/2))/2)**n)) / (5)**(1/2))

n = 1
sum = 0

while True:
    fibonaciNumber = fibonaci(n)

    if fibonaciNumber > 4_000_000:
        break

    if fibonaciNumber % 2 == 0:
        sum += fibonaciNumber

    n += 1

print(sum)