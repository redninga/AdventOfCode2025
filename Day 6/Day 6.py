file = open("input.txt","r")
content =file.read()
file.close()
code = content.split('\n')

import numpy as np
import copy

#%% part 1
# spaties verwijderen
code2 = []
for line in code:
    code2.append([i for i in line.split(" ") if i != ""])

numbers = code2[:-1]
symbols = code2[-1]

# op basis van symbol de volgende nummer reeks pakken
answers = []
for n in range(len(symbols)):
    # als keer som dan antwoord 1 als basis
    if symbols[n] == "*":
        answer = 1
        for i in numbers:
            answer *= int(i[n])
    # als plus sum dan antwoord 0 als basis
    elif symbols[n] == "+":
        answer = 0
        for i in numbers:
            answer += int(i[n])
    # antwoord toevoegen
    answers.append(answer)
print(sum(answers))

#%% part 2
# 2d array met begin en eindpunten van grids bepalen
symbols = code[-1]
lengths = []
start = [0]
symbols2 = [symbols[0]]
n = 0
for n in range(1,len(symbols)):
    if symbols[n] != " ":
        symbols2.append(symbols[n])
        lengths.append(n - start[-1] - 1)
        start.append(n)
lengths.append(n - start[-1] + 1)    


numbers = np.array([list(i) for i in code[:-1]])
answers = []
# loopen over alle start momenten etc.
for n in range(len(start)):
    # grid creeren op basis van de info
    grid = numbers[:,start[n]:(start[n] + lengths[n])]
    # print(grid)
    # keer som antwoord 1 en dan waardes uit grid halen
    if symbols2[n] == "*":
        answer = 1
        for m in range(len(grid[0,:])):
            answer *= int("".join(grid[:,m]))
            # print(grid[:,m])
    # plus som antwoord 1 en dan waardes uit grid halen
    elif symbols2[n] == "+":
        answer = 0
        for m in range(len(grid[0,:])):
            answer += int("".join(grid[:,m]))
    answers.append(answer)
print(sum(answers))




# answers = []
# for n in range(len(symbols)):
#     grid = np.zeros((3,3))
#     for i in numbers:
#         pass
#     if symbols[n] == "*":
        
#         answer = 1
        
#     elif symbols[n] == "+":
#         answer = 0
#         for i in numbers:
#             answer += int(i[n])
#     answers.append(answer)
# print(sum(answers))

# #%% part 2

# # soorteren id's op basis van start
# newminrange = []
# newmaxrange = []
# minrange,maxrange = zip(*sorted(zip(minrange, maxrange)))
# n = 0
# start = 0
# end  = 0
# # Life is pain

# # loop over alle ranges heen
# for m in range(0,len(freshranges)):
#     # als de range start groter is dan het vorige einde dan begint er nieuwe range
#     if end < minrange[m]:
#         start = minrange[m]
#         end = copy.deepcopy(maxrange[m])
#         # loop over alle komende ranges heen
#         for n in range(m+1,len(freshranges)):
#             # als het einde evengroot of kleiner is dan de start en de 
#             if end >= minrange[n] and end < maxrange[n]:
#                 end = copy.deepcopy(maxrange[n])
#         newminrange.append(copy.deepcopy(start))
#         newmaxrange.append(copy.deepcopy(end))
# total = np.dtype('int64').type(0)
# for n in range(len(newmaxrange)):
#     total += newmaxrange[n]+1 - newminrange[n]
#     # for i in range(newminrange[n],newmaxrange[n]+1):
#     #     print(i)

# # for n in range(len(newmaxrange)-1):
# #     print(newmaxrange[n+1] -newmaxrange[n])

# print(total)
# # ids = []
# # for n in range(len(freshranges)):
# #     print(n)
# #     for i in range(minrange[n],maxrange[n]+1):
# #         if not i in ids:
# #            ids.append(i)
# # print(len(ids))
# #%% part 1

# # # legen lijsten maken
# # grid = np.zeros((len(code) + 2, len(code[0]) +2))
# # answer = np.zeros((len(code) + 2, len(code[0]) +2))

# # # grid vullen
# # for n,i in enumerate(code):
# #     for m,j in enumerate(i):
# #         if j == "@":
# #             grid[n+1,m+1] = 1

# # # loop over het grid
# # for n in range(len(code)):
# #     for m in range(len(code[0])):
# #         # als er een rol staat op het huidige coordinaat
# #         if grid[n+1,m+1] == 1:
# #             # als er in een 3x3 radius 4 of minder rollen zijn (zichzelf + 3 andere) dan kan deze verwijderd worden
# #             if sum(sum(grid[n:(n+3),m:(m+3)])) <= 4:
# #                 answer[n+1,m+1] = 1
                
# # print(sum(sum(answer)))

# #%% part 2
# # totalanswer = 0
# # grid = np.zeros((len(code) + 2, len(code[0]) +2))

# # # grid vullen
# # for n,i in enumerate(code):
# #     for m,j in enumerate(i):
# #         if j == "@":
# #             grid[n+1,m+1] = 1
            
# # # door gaan tot er veranding is
# # while(True):
# #     # leeg answer elke loop
# #     answer = np.zeros((len(code) + 2, len(code[0]) +2))
# #     # loop over de grid
# #     for n in range(len(code)):
# #         for m in range(len(code[0])):
# #             # als er een rol staat op het huidige coordinaat
# #             if grid[n+1,m+1] == 1:
# #                 # als er in een 3x3 radius 4 of minder rollen zijn (zichzelf + 3 andere) dan kan deze verwijderd worden
# #                 if sum(sum(grid[n:(n+3),m:(m+3)])) <= 4:
# #                     # theoretisch kan je nu ook grid updaten direct
# #                     answer[n+1,m+1] = 1
    
# #     # som opslaan
# #     totalanswer += sum(sum(answer))
# #     # nieuw grid maken (kan in theorie mid loop)
# #     grid = grid - answer
# #     # break als er geen verandering is
# #     if sum(sum(answer)) == 0:
# #         break
# # print(totalanswer)

