translater = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
              10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 
              17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
              60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "onehundred", 200: "twohundred", 
              300: "threehundred", 400: "fourhundred", 500: "fivehundred", 600: "sixhundred", 700: "sevenhundred",
              800: "eighthundred", 900: "ninehundred", 1000: "onethousand"}

def decodeBetween1and99(n):
    if n % 10 == 0:
        return translater[n]
    
    if n < 100:
        if n < 10:
            return translater[n]
        elif n < 20:
            return translater[n]
        else:
            partOne = translater[int(str(n)[0])*10]
            partTwo = translater[int(str(n)[1])]

            return partOne+partTwo

def turnIntoWords(n):
    if n % 100 == 0:
        return translater[n]
    
    if n < 100:
        return decodeBetween1and99(n)
    
    hundredsPart = str(translater[n // 100 * 100])
    n -= (n // 100 * 100)
    return hundredsPart + "and" + decodeBetween1and99(n)

totalString = ""

for i in range(1, 1001):
    totalString += turnIntoWords(i)

print(len(totalString))