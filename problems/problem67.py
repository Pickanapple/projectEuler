triangle = []

with open("67_triangle.txt") as file:
    t = file.readlines()

    for i in t: 
        triangle.append(list(map(int, i.replace("\n", "").split())))
    
    print(triangle)

def solveFromBottom(triangle): 
    for i in range(len(triangle) - 1, 0, -1):
        for j in range(len(triangle[i]) - 1):
            triangle[i - 1][j] += max(triangle[i][j], triangle[i][j + 1])

    print(triangle[0])

solveFromBottom(triangle)