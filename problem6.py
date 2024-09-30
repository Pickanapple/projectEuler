def sumOfSquares(n):
    sum = 0 
    for i in range(n+1):
        sum += i**2
    return sum

def squareOfSum(n):
    return ((n+1)*(n//2))**2

if __name__ == "__main__":
    print(squareOfSum(100) - sumOfSquares(100))