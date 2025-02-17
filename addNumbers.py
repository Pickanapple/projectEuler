with open("README.md") as f:
    lines = f.readlines()

with open("README.md", "w") as f:
    i = 1
    for j in lines: 
        if j[0] == "-":
            j = j.replace("] ", f"] {i}. ")

            i += 1
        f.write(f"{j}")