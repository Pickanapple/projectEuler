def triangle(n: int) -> int:
    return ((n + 1) * n) // 2

def divisorsCount(n):
    count = 2 #Every one has 1 and itself, so we can include that
    
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    
    found = []

    for i in range(2, round(n**(1/2)) + 1):
        if i not in found:
            if n % i == 0:
                if n % i != i:
                    count += 2
                    found.append(i)
                    found.append(n/i)
                else:
                    count += 1
                    found.append(i)
    
    return count

print(divisorsCount(triangle(7)))

i = 8 #We are given the first 7

while True:
    print(i)
    triangleNumber = triangle(i)
    if divisorsCount(triangleNumber) >= 500:
        print(triangleNumber)

    i += 1