def isPalindrome(n):
    n = str(n)
    if n[::-1] == n:
        return True
    
def palindromeNumber():
    """
    Brute forcing the highest palindrome
    """
    palindromes = []

    for i in range (999, 800, -1):
        for j in range (999, 800, -1):
            if isPalindrome(i * j):
                palindromes.append(i*j)

    return max(palindromes)

print(palindromeNumber())