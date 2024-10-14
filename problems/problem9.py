from math import sqrt

def triplet():
    for i in range (2, 500):
        for j in range(1, i):
            if int(sqrt((i**2) + (j**2))) == sqrt((i**2) + (j**2)):
                if i + j + sqrt(i**2 + j**2) == 1000:
                    return i * j * sqrt(i**2 + j**2)

print(triplet())