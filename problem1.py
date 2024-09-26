def sumOfMultiples(start=0, end=20, *multiples):
    correctMultiples = 0
    for i in range(start, end+1):
        for j in multiples:
            if i%j == 0:
                correctMultiples += i
                break
    
    return correctMultiples

print(sumOfMultiples(0, 999, 3, 5))