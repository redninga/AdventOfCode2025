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

