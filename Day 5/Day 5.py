file = open("input.txt","r")
content =file.read()
file.close()
code = content.split('\n\n')

import numpy as np
import copy

# info uit data krijgen
freshranges = code[0].split('\n')
items = code[1].split('\n')
freshranges = [i.split('-') for i in freshranges]
maxrange = [np.dtype('int64').type(i[1]) for i in freshranges]
minrange = [np.dtype('int64').type(i[0]) for i in freshranges]

# waardes om aantal id's op te slaan
fresh = 0
freshids = []
spoiledids = []
# loop over items
for i in items:
    # loop over ranges
    for n in range(len(freshranges)):
        # als waarde binnen range valt dan fresh anders niet fresh
        if int(i) >= minrange[n] and int(i) <= maxrange[n]:
            fresh += 1
            freshids.append(int(i))
            break
        if n == len(freshranges)-1:
            spoiledids.append(int(i))
print(fresh)

#%% part 2

# soorteren id's op basis van start
newminrange = []
newmaxrange = []
minrange,maxrange = zip(*sorted(zip(minrange, maxrange)))
n = 0
start = 0
end  = 0
# Life is pain

# loop over alle ranges heen
for m in range(0,len(freshranges)):
    # als de range start groter is dan het vorige einde dan begint er nieuwe range
    if end < minrange[m]:
        start = minrange[m]
        end = copy.deepcopy(maxrange[m])
        # loop over alle komende ranges heen
        for n in range(m+1,len(freshranges)):
            # als het einde evengroot of kleiner is dan de start en de 
            if end >= minrange[n] and end < maxrange[n]:
                end = copy.deepcopy(maxrange[n])
        newminrange.append(copy.deepcopy(start))
        newmaxrange.append(copy.deepcopy(end))
total = np.dtype('int64').type(0)
for n in range(len(newmaxrange)):
    total += newmaxrange[n]+1 - newminrange[n]
    # for i in range(newminrange[n],newmaxrange[n]+1):
    #     print(i)

# for n in range(len(newmaxrange)-1):
#     print(newmaxrange[n+1] -newmaxrange[n])

print(total)
# ids = []
# for n in range(len(freshranges)):
#     print(n)
#     for i in range(minrange[n],maxrange[n]+1):
#         if not i in ids:
#            ids.append(i)
# print(len(ids))
#%% part 1

# # legen lijsten maken
# grid = np.zeros((len(code) + 2, len(code[0]) +2))
# answer = np.zeros((len(code) + 2, len(code[0]) +2))

# # grid vullen
# for n,i in enumerate(code):
#     for m,j in enumerate(i):
#         if j == "@":
#             grid[n+1,m+1] = 1

# # loop over het grid
# for n in range(len(code)):
#     for m in range(len(code[0])):
#         # als er een rol staat op het huidige coordinaat
#         if grid[n+1,m+1] == 1:
#             # als er in een 3x3 radius 4 of minder rollen zijn (zichzelf + 3 andere) dan kan deze verwijderd worden
#             if sum(sum(grid[n:(n+3),m:(m+3)])) <= 4:
#                 answer[n+1,m+1] = 1
                
# print(sum(sum(answer)))

#%% part 2
# totalanswer = 0
# grid = np.zeros((len(code) + 2, len(code[0]) +2))

# # grid vullen
# for n,i in enumerate(code):
#     for m,j in enumerate(i):
#         if j == "@":
#             grid[n+1,m+1] = 1
            
# # door gaan tot er veranding is
# while(True):
#     # leeg answer elke loop
#     answer = np.zeros((len(code) + 2, len(code[0]) +2))
#     # loop over de grid
#     for n in range(len(code)):
#         for m in range(len(code[0])):
#             # als er een rol staat op het huidige coordinaat
#             if grid[n+1,m+1] == 1:
#                 # als er in een 3x3 radius 4 of minder rollen zijn (zichzelf + 3 andere) dan kan deze verwijderd worden
#                 if sum(sum(grid[n:(n+3),m:(m+3)])) <= 4:
#                     # theoretisch kan je nu ook grid updaten direct
#                     answer[n+1,m+1] = 1
    
#     # som opslaan
#     totalanswer += sum(sum(answer))
#     # nieuw grid maken (kan in theorie mid loop)
#     grid = grid - answer
#     # break als er geen verandering is
#     if sum(sum(answer)) == 0:
#         break
# print(totalanswer)

