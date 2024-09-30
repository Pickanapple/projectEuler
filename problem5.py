def evenlyDivsible(n, lower=1, upper=20):
    for i in range (lower, upper+1):
        if n % i != 0:
            return False
        
    return True

if __name__ == "__main__":

    i = 1

    while evenlyDivsible(i) == False:
        i += 1

    print(i)