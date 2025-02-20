alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open ("data/NAMES.txt") as n: 
    names = list(n.readline().replace("\"", "").replace("\n", "").split(","))
    names.sort()

total = 0

for i in range(1, len(names) + 1):
    sum = 0
    
    for j in names[i - 1]:
        sum += alphabet.index(j) + 1
    
    total += sum * i

print(total)
