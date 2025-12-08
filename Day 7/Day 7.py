file = open("input.txt","r")
content =file.read()
file.close()
code = content.split('\n')

import numpy as np
import copy

#%% part 1
# spaties verwijderen

code2 = np.array([list(x) for x in code])
for n in range(1,len(code2[:,0])):
    for m in range(1,len(code2[n,:])-1):
        if code2[n-1,m] == "S":
            code2[n,m] = "1"
            print(n,m)
        if code2[n-1,m] == "1":
            if code2[n,m] == "^":
                code2[n,m-1] = "1"
                code2[n,m+1] = "1"
                code2[n,m] = "X"
            if code2[n,m] == ".":
                code2[n,m] = 1

print((code2 == "X").sum())

#%% part 2
code2 = np.array([list(x) for x in code],dtype=object)
code2[code2 == "."] = 0

for n in range(1,len(code2[:,0])):
    for m in range(len(code2[n,:])):
        if code2[n-1,m] == "S":
            code2[n,m] = "1"
            print(n,m)
        if code2[n-1,m] != "0" and code2[n-1,m] != "^" and code2[n-1,m] != "S" and code2[n-1,m] != "X":
            if code2[n,m] == "^":
                # print(n,int(code2[n,m-1]) + int(code2[n-1,m]),int(code2[n,m+1]) + int(code2[n-1,m]))
                code2[n,m-1] = int(code2[n,m-1]) + int(code2[n-1,m])
                code2[n,m+1] = int(code2[n,m+1]) + int(code2[n-1,m])
                code2[n,m] = "X"
            else:
                code2[n,m] = int(code2[n-1,m]) + int(code2[n,m])
            
            

print(sum([int(x) for x in code2[-1,:]]))

# for line in code:
#     code2.append([i for i in line.split(" ") if i != ""])

# numbers = code2[:-1]
# symbols = code2[-1]

# # op basis van symbol de volgende nummer reeks pakken
# answers = []
# for n in range(len(symbols)):
#     # als keer som dan antwoord 1 als basis
#     if symbols[n] == "*":
#         answer = 1
#         for i in numbers:
#             answer *= int(i[n])
#     # als plus sum dan antwoord 0 als basis
#     elif symbols[n] == "+":
#         answer = 0
#         for i in numbers:
#             answer += int(i[n])
#     # antwoord toevoegen
#     answers.append(answer)
# print(sum(answers))

# #%% part 2
# # 2d array met begin en eindpunten van grids bepalen
# symbols = code[-1]
# lengths = []
# start = [0]
# symbols2 = [symbols[0]]
# n = 0
# for n in range(1,len(symbols)):
#     if symbols[n] != " ":
#         symbols2.append(symbols[n])
#         lengths.append(n - start[-1] - 1)
#         start.append(n)
# lengths.append(n - start[-1] + 1)    


# numbers = np.array([list(i) for i in code[:-1]])
# answers = []
# # loopen over alle start momenten etc.
# for n in range(len(start)):
#     # grid creeren op basis van de info
#     grid = numbers[:,start[n]:(start[n] + lengths[n])]
#     # print(grid)
#     # keer som antwoord 1 en dan waardes uit grid halen
#     if symbols2[n] == "*":
#         answer = 1
#         for m in range(len(grid[0,:])):
#             answer *= int("".join(grid[:,m]))
#             # print(grid[:,m])
#     # plus som antwoord 1 en dan waardes uit grid halen
#     elif symbols2[n] == "+":
#         answer = 0
#         for m in range(len(grid[0,:])):
#             answer += int("".join(grid[:,m]))
#     answers.append(answer)
# print(sum(answers))


