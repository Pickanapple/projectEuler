# primes = [2, 3, 5, 7]

# def isPrime(n):
#     if n in primes:
#         return True

#     if n == 2:
#         return True
    
#     if n < 2:
#         return False
    
#     for i in primes:
        
#         if n % i == 0:
#             return False
#         elif i == primes[-1]:
#             primes.append(n)
#             return True
    
# sum = 17

# list = [i for i in range(9, 2_000_000, 2)]

# for i in list:
#     print(i)
#     if isPrime(i):
#         sum += i

# print(f"Completed! The sum is {sum}")

#Using Sieve of Eratoshenes
# Such a slow brute force, but it works and I am not going to make it more efficient now!
list = [i for i in range(2, 2_000_000)]
startValue = 0
offset = 0 
# print(list)
primes = []

while list:
    try:
        while list[startValue] == "removed":
            startValue += 1
            offset += 1
    except:
        print(primes)
        print(sum(primes))
        break
    i = list[startValue]

    step = i
    while len(list) > step + offset:
        list[step+offset] = "removed"
        step += i
        # print(step)
    primes.append(list.pop(startValue))

    print(i)