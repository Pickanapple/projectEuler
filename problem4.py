def isPalindrome(n):
    n = str(n)
    if n[::-1] == n:
        return True

for i in range (999, 0, -1):
    if isPalindrome(i * 999):
        answer = i * 999
        break

print(answer)