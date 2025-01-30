#https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
from math import floor

def calculateDay(d, m, Y):
    m -= 2
    if m <= 0:
        m += 12

    if m == 11 or m == 12:
        Y -= 1
    
    c = floor(Y/100)
    y = Y - 100*c

    return (d + floor(2.6*m - 0.2) + y + floor(y / 4) + floor(c / 4) - 2 * c) % 7

count = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if calculateDay(1, j, i) == 0:
            count += 1

print(count)