file = open("input2.txt","r")
content =file.read()
file.close()
code = content.split('\n')

import numpy as np
import copy
import re

indicator = []
schematics = []
joltage = []

for i in code:
    i = re.sub(r'[{}\[\]()]', '', i)
    i = i.split(" ")
    ind = []
    for j in i[0]:
        ind.append(j == "#")
    indicator.append(ind)
    schem = []
    for j in i[1:-1]:
        if len(j) == 1:
            schem.append([int(j)])
        else:
            schem.append([int(x) for x in j.split(",")])
    schematics.append(schem)
    jolt = []
    for j in i[-1].split(","):
        jolt.append(int(j))
    joltage.append(jolt)

minanswers = []
for n in range(len(code)):
    xz = np.zeros((len(indicator[n]),len(schematics[n])),dtype = bool)
    # print(xz)
    for m,x in enumerate(schematics[n]):
        # print(m,x)
        for x1 in x:
            xz[x1-1,m] = True
    print(xz)
    # for m in range(len(schematics))
        