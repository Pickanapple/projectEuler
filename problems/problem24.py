from itertools import permutations

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
perms = list(permutations(digits))

perms.sort()

print(perms[999_999])