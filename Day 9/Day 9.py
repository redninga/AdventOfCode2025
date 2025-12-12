file = open("input.txt","r")
content =file.read()
file.close()
code = content.split('\n')

import numpy as np
import copy

#%% part 1
# spaties verwijderen

points = [list(map(int, x.split(","))) for x in code]

distance = np.zeros((len(points),len(points)),dtype = np.int64)

for n in range(len(points)):
    for m in range(n+1,len(points)):
        dis = (abs(points[n][0] - points[m][0]) + 1) * (abs(points[n][1] - points[m][1]) + 1)
        distance[n,m] = dis
maximum = np.argwhere(distance == np.max(distance))[0]
print(maximum)
print(distance[maximum[0],maximum[1]])

#%% part 2


grid = np.zeros((max([x[0] for x in points])+3,max([x[1] for x in points])+3),dtype = bool)
grid2 = copy.deepcopy(grid)

for n in range(0,len(points)):
    m = n-1
    if points[n][0] - points[m][0] == 0:
        if points[n][1] < points[m][1]:
            grid[points[n][0],points[n][1]:(points[m][1]+1)] = True
        else:
            grid[points[n][0],points[m][1]:(points[n][1]+1)] = True
    else:
        if points[n][0] < points[m][0]:
            grid[points[n][0]:(points[m][0]+1),points[n][1]] = True
        else:
            grid[points[m][0]:(points[n][0]+1), points[n][1]] = True

size = grid.shape

spread = np.argwhere(grid == True)
for i in spread:
    for j in range(i[0]-1,i[0]+2):
        for k in range(i[1]-1,i[1]+2):
            if not grid[j,k]:
                grid2[j,k] = True


spread = [[points[0][0]+1,points[0][1]-1]]
grid2[spread[0][0],spread[0][1]] = False
counter = 0
while(len(spread) != 0):
    counter += 1
    spread2 = []
    for i in spread:
        if (i[0] != size[0]-1):
            if not grid[i[0]+1 ,i[1]] and grid2[i[0]+1 ,i[1]]:
                spread2.append([i[0]+1 ,i[1]])
                grid2[i[0]+1 ,i[1]] = False
        if (i[0] != 0):
            if not grid[i[0]-1 ,i[1]] and grid2[i[0]-1 ,i[1]]:
                spread2.append([i[0]-1 ,i[1]])
                grid2[i[0]-1 ,i[1]] = False
        if (i[1] != size[1]-1):
            if not grid[i[0],i[1]+1] and grid2[i[0] ,i[1]+1]:
                spread2.append([i[0] ,i[1]+1])
                grid2[i[0] ,i[1]+1] = False
        if (i[1] != 0):
            if not grid[i[0] ,i[1]-1] and grid2[i[0],i[1]-1]:
                spread2.append([i[0] ,i[1]-1])
                grid2[i[0] ,i[1]-1] = False
    # print(len(spread2),counter)
    spread = spread2
#%%

for n in range(len(points)):
    for m in range(n+1,len(points)):
        dis = (grid2[points[n][0]:(points[m][0] + 1),points[n][1]].any() + 
               grid2[points[n][0]:(points[m][0] + 1),points[m][1]].any() +
               grid2[points[m][0]:(points[n][0] + 1),points[n][1]].any() + 
               grid2[points[m][0]:(points[n][0] + 1),points[m][1]].any() +
               grid2[points[n][0],points[n][1]:(points[m][1] + 1)].any() + 
               grid2[points[m][0],points[n][1]:(points[m][1] + 1)].any() +
               grid2[points[n][0],points[m][1]:(points[n][1] + 1)].any() + 
               grid2[points[m][0],points[m][1]:(points[n][1] + 1)].any())
        # dis = grid2[points[n][0]:(points[m][0] + 1),points[n][1]:(points[m][1]+1)].any() + grid2[points[m][0]:(points[n][0] + 1),points[n][1]:(points[m][1]+1)].any() + grid2[points[n][0]:(points[m][0] + 1),points[m][1]:(points[n][1]+1)].any() + grid2[points[m][0]:(points[n][0] + 1),points[m][1]:(points[n][1]+1)].any() 
        print(n,m,dis)
        if dis != 0:
            distance[n,m] = 0
        
maximum = np.argwhere(distance == np.max(distance))[0]
print(maximum)
print(distance[maximum[0],maximum[1]])


#%%

            
#         if (i[0] != size[0]-1):
#             if not grid[i[0]+1 ,i[1]] and not grid2[i[0]+1 ,i[1]]:
#                 spread2.append([i[0]+1 ,i[1]])
#                 grid2[i[0]+1 ,i[1]] = True
#         if (i[0] != 0):
#             if not grid[i[0]-1 ,i[1]] and not grid2[i[0]-1 ,i[1]]:
#                 spread2.append([i[0]-1 ,i[1]])
#                 grid2[i[0]-1 ,i[1]] = True
#         if (i[1] != size[1]-1):
#             if not grid[i[0],i[1]+1] and not grid2[i[0] ,i[1]+1]:
#                 spread2.append([i[0] ,i[1]+1])
#                 grid2[i[0] ,i[1]+1] = True
#         if (i[1] != 0):
#             if not grid[i[0] ,i[1]-1] and not grid2[i[0],i[1]-1]:
#                 spread2.append([i[0] ,i[1]-1])
#                 grid2[i[0] ,i[1]-1] = True
#     print(len(spread2),counter)
#     spread = spread2



# #%%            
# for n in range(len(points)):
#     for m in range(n+1,len(points)):
#         for p in range(len(points)):
#             print(n,m,p)
#             if (points[n][0] < points[p][0] < points[m][0] or points[m][0] < points[p][0] < points[n][0]) and (points[n][1] < points[p][1] < points[m][1] or points[m][1] < points[p][1] < points[n][1]):
#                 distance[n,m] = 0

# maximum = np.argwhere(distance == np.max(distance))[0]
# print(maximum)
# print(distance[maximum[0],maximum[1]])


# #%% part 2


# grid = np.zeros((max([x[0] for x in points])+2,max([x[1] for x in points])+2),dtype = bool)
# grid2 = copy.deepcopy(grid)

# for n in range(0,len(points)):
#     m = n-1
#     if points[n][0] - points[m][0] == 0:
#         if points[n][1] < points[m][1]:
#             grid[points[n][0],points[n][1]:(points[m][1]+1)] = True
#         else:
#             grid[points[n][0],points[m][1]:(points[n][1]+1)] = True
#     else:
#         if points[n][0] < points[m][0]:
#             grid[points[n][0]:(points[m][0]+1),points[n][1]] = True
#         else:
#             grid[points[m][0]:(points[n][0]+1), points[n][1]] = True

# for n in range(len(points)):
#     for m in range(n+1,len(points)):
#         print(n,m)
#         if points[n][0] < points[m][0]:
#             if points[n][1] < points[m][1]:
#                 if grid[(points[n][0]+1):points[m][0],(points[n][1]+1):points[m][1]].sum() != 0:
#                     distance[n,m] = 0
#             elif points[n][1] > points[m][1]:
#                 if grid[(points[n][0]+1):points[m][0],(points[m][1]+1):points[n][1]].sum() != 0:
#                     distance[n,m] = 0
#         elif points[n][0] > points[m][0]:
#             if points[n][1] < points[m][1]:
#                 if grid[(points[m][0]+1):points[n][0],(points[n][1]+1):points[m][1]].sum() != 0:
#                     distance[n,m] = 0
#             elif points[n][1] > points[m][1]:
#                 if grid[(points[m][0]+1):points[n][0],(points[m][1]+1):points[n][1]].sum() != 0:
#                     distance[n,m] = 0
       




# #%% part 2 failed
# grid = np.zeros((max([x[0] for x in points])+2,max([x[1] for x in points])+2),dtype = bool)
# grid2 = copy.deepcopy(grid)


# for n in range(0,len(points)):
#     m = n-1
#     if points[n][0] - points[m][0] == 0:
#         if points[n][1] < points[m][1]:
#             grid[points[n][0],points[n][1]:(points[m][1]+1)] = True
#         else:
#             grid[points[n][0],points[m][1]:(points[n][1]+1)] = True
#     else:
#         if points[n][0] < points[m][0]:
#             grid[points[n][0]:(points[m][0]+1),points[n][1]] = True
#         else:
#             grid[points[m][0]:(points[n][0]+1), points[n][1]] = True

# size = grid.shape
# spread = [[0,0]]
# counter = 0
# while(len(spread) != 0):
#     counter += 1
#     spread2 = []
#     for i in spread:
#         if (i[0] != size[0]-1):
#             if not grid[i[0]+1 ,i[1]] and not grid2[i[0]+1 ,i[1]]:
#                 spread2.append([i[0]+1 ,i[1]])
#                 grid2[i[0]+1 ,i[1]] = True
#         if (i[0] != 0):
#             if not grid[i[0]-1 ,i[1]] and not grid2[i[0]-1 ,i[1]]:
#                 spread2.append([i[0]-1 ,i[1]])
#                 grid2[i[0]-1 ,i[1]] = True
#         if (i[1] != size[1]-1):
#             if not grid[i[0],i[1]+1] and not grid2[i[0] ,i[1]+1]:
#                 spread2.append([i[0] ,i[1]+1])
#                 grid2[i[0] ,i[1]+1] = True
#         if (i[1] != 0):
#             if not grid[i[0] ,i[1]-1] and not grid2[i[0],i[1]-1]:
#                 spread2.append([i[0] ,i[1]-1])
#                 grid2[i[0] ,i[1]-1] = True
#     print(len(spread2),counter)
#     spread = spread2
# grid3 = np.invert(grid2)

# distance2 = np.zeros((len(points),len(points)),dtype = np.int64)

# for n in range(len(points)):
#     for m in range(n+1,len(points)):
#         dis = grid3[points[n][0]:(points[m][0] + 1),points[n][1]:(points[m][1]+1)].sum() + grid3[points[m][0]:(points[n][0] + 1),points[n][1]:(points[m][1]+1)].sum() + grid3[points[n][0]:(points[m][0] + 1),points[m][1]:(points[n][1]+1)].sum() + grid3[points[m][0]:(points[n][0] + 1),points[m][1]:(points[n][1]+1)].sum() 
#         distance2[n,m] = dis
        
# distance3 = distance * (distance == distance2)
# maximum = np.argwhere(distance3 == np.max(distance3))[0]
# print(maximum)
# print(distance3[maximum[0],maximum[1]])     
# # locs = np.array(list(range(len(points))))

# # for n in range(len(points)):
# #     distance[n,n] = 100000000000
# #     for m in range(n+1,len(points)):
# #         dis = (points[n][0] - points[m][0]) ** 2 + (points[n][1] - points[m][1]) ** 2 + (points[n][2] - points[m][2]) ** 2 
# #         distance[n,m] = dis
# #         distance[m,n] = dis
        
# # for n in range(999):
# #     print(n)
# #     mindis = np.argwhere(distance == np.min(distance))[0]
# #     for i in np.where(ids == ids[mindis[1]])[0]:
# #         for j in np.where(ids == ids[mindis[0]])[0]:
# #             # print(i,j)
# #             # distance[i,j] = 100000000000
# #             # distance[j,i] = 100000000000
# #             ids[j] = ids[i]
# #     distance[mindis[0],mindis[1]] = 100000000000
# #     distance[mindis[1],mindis[0]] = 100000000000
# #     #ids[np.where(ids == ids[mindis[1]])] = ids[mindis[0]] 
# #     # print(ids,mindis)
    

# # amount = []
# # for x in np.unique(ids):
# #     amount.append(sum(ids == x))
# #     print(x, sum(ids == x))
# # print(sorted(zip(amount))[-3:])
# # answer = 1
# # for x in sorted(zip(amount))[-3:]:
# #     answer *= x[0]
# # print(answer)
# # #%%
# # distance = np.zeros((len(points),len(points)),dtype = np.int64)
# # ids = np.array(list(range(len(points))))

# # for n in range(len(points)):
# #     distance[n,n] = 100000000000
# #     for m in range(n+1,len(points)):
# #         dis = (points[n][0] - points[m][0]) ** 2 + (points[n][1] - points[m][1]) ** 2 + (points[n][2] - points[m][2]) ** 2 
# #         distance[n,m] = dis
# #         distance[m,n] = dis



# # for n in range(999):
# #     print(n)
# #     mindis = np.argwhere(distance == np.min(distance))[0]
# #     for i in np.where(ids == ids[mindis[1]])[0]:
# #         for j in np.where(ids == ids[mindis[0]])[0]:
# #             # print(i,j)
# #             distance[i,j] = 100000000000
# #             distance[j,i] = 100000000000
# #             ids[j] = ids[i]
# #     # distance[mindis[0],mindis[1]] = 100000000000
# #     # distance[mindis[1],mindis[0]] = 100000000000
# #     #ids[np.where(ids == ids[mindis[1]])] = ids[mindis[0]] 
# #     #print(ids,mindis)
    
# # print(mindis)
# # print(points[mindis[0]][0]*points[mindis[1]][0])