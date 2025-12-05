file = open("input2.txt","r")
content =file.read()
file.close()
code = content.split('\n\n')

import numpy as np

freshranges = code[0].split('\n')
items = code[1].split('\n')
freshranges = [i.split('-') for i in freshranges]
maxrange = [int(i[1]) for i in freshranges]
minrange = [int(i[0]) for i in freshranges]
fresh = 0
freshids = []
spoiledids = []
for i in items:
    for n in range(len(freshranges)):
        if int(i) >= minrange[n] and int(i) <= maxrange[n]:
            fresh += 1
            freshids.append(int(i))
            break
        if n == len(freshranges)-1:
            spoiledids.append(int(i))
print(fresh)

#%% part 2
newminrange = []
newmaxrange = []
minrange,maxrange = zip(*sorted(zip(minrange, maxrange)))
n = 0
while (True):
    i
for n in range(1,len(freshranges)):
    pass
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

