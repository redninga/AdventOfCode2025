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
ids = np.array(list(range(len(points))))

for n in range(len(points)):
    distance[n,n] = 100000000000
    for m in range(n+1,len(points)):
        dis = (points[n][0] - points[m][0]) ** 2 + (points[n][1] - points[m][1]) ** 2 + (points[n][2] - points[m][2]) ** 2 
        distance[n,m] = dis
        distance[m,n] = dis
        
for n in range(999):
    print(n)
    mindis = np.argwhere(distance == np.min(distance))[0]
    for i in np.where(ids == ids[mindis[1]])[0]:
        for j in np.where(ids == ids[mindis[0]])[0]:
            # print(i,j)
            # distance[i,j] = 100000000000
            # distance[j,i] = 100000000000
            ids[j] = ids[i]
    distance[mindis[0],mindis[1]] = 100000000000
    distance[mindis[1],mindis[0]] = 100000000000
    #ids[np.where(ids == ids[mindis[1]])] = ids[mindis[0]] 
    # print(ids,mindis)
    

amount = []
for x in np.unique(ids):
    amount.append(sum(ids == x))
    print(x, sum(ids == x))
print(sorted(zip(amount))[-3:])
answer = 1
for x in sorted(zip(amount))[-3:]:
    answer *= x[0]
print(answer)
#%%
distance = np.zeros((len(points),len(points)),dtype = np.int64)
ids = np.array(list(range(len(points))))

for n in range(len(points)):
    distance[n,n] = 100000000000
    for m in range(n+1,len(points)):
        dis = (points[n][0] - points[m][0]) ** 2 + (points[n][1] - points[m][1]) ** 2 + (points[n][2] - points[m][2]) ** 2 
        distance[n,m] = dis
        distance[m,n] = dis



for n in range(999):
    print(n)
    mindis = np.argwhere(distance == np.min(distance))[0]
    for i in np.where(ids == ids[mindis[1]])[0]:
        for j in np.where(ids == ids[mindis[0]])[0]:
            # print(i,j)
            distance[i,j] = 100000000000
            distance[j,i] = 100000000000
            ids[j] = ids[i]
    # distance[mindis[0],mindis[1]] = 100000000000
    # distance[mindis[1],mindis[0]] = 100000000000
    #ids[np.where(ids == ids[mindis[1]])] = ids[mindis[0]] 
    #print(ids,mindis)
    
print(mindis)
print(points[mindis[0]][0]*points[mindis[1]][0])

# amount = []
# for x in np.unique(ids):
#     amount.append(sum(ids == x))
#     print(x, sum(ids == x))
# print(sorted(zip(amount))[-3:])
# answer = 1
# for x in sorted(zip(amount))[-3:]:
#     answer *= x[0]
# print(answer)
# code2 = np.array([list(x) for x in code])
# for n in range(1,len(code2[:,0])):
#     for m in range(1,len(code2[n,:])-1):
#         if code2[n-1,m] == "S":
#             code2[n,m] = "1"
#             print(n,m)
#         if code2[n-1,m] == "1":
#             if code2[n,m] == "^":
#                 code2[n,m-1] = "1"
#                 code2[n,m+1] = "1"
#                 code2[n,m] = "X"
#             if code2[n,m] == ".":
#                 code2[n,m] = 1

# print((code2 == "X").sum())

# #%% part 2
# code2 = np.array([list(x) for x in code],dtype=object)
# code2[code2 == "."] = 0

# for n in range(1,len(code2[:,0])):
#     for m in range(len(code2[n,:])):
#         if code2[n-1,m] == "S":
#             code2[n,m] = "1"
#             print(n,m)
#         if code2[n-1,m] != "0" and code2[n-1,m] != "^" and code2[n-1,m] != "S" and code2[n-1,m] != "X":
#             if code2[n,m] == "^":
#                 # print(n,int(code2[n,m-1]) + int(code2[n-1,m]),int(code2[n,m+1]) + int(code2[n-1,m]))
#                 code2[n,m-1] = int(code2[n,m-1]) + int(code2[n-1,m])
#                 code2[n,m+1] = int(code2[n,m+1]) + int(code2[n-1,m])
#                 code2[n,m] = "X"
#             else:
#                 code2[n,m] = int(code2[n-1,m]) + int(code2[n,m])
            
            

# print(sum([int(x) for x in code2[-1,:]]))


