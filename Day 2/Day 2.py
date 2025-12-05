file = open("input.txt","r")
content =file.read()
file.close()
code = content.split(',')

#%% part 1
invalid = []
# loop over ranges
for ids in code:
    [start,end] = ids.split('-')
    start = int(start)
    end = int(end)
    # loop over de ID's
    for i in range(start,end+1):
        j = str(i)
        length = len(j)
        # als ID een even lengte heeft dan vergelijk de 2 helften
        if length % 2 == 0:
            part1 = j[int(length/2):]
            part2 = j[:int(length/2)]
            if part1 == part2:
                invalid.append(int(j))
answer1 = sum(invalid)
print(answer1)

#%% part 1
invalid = []
# loop over ranges
for ids in code:
    [start,end] = ids.split('-')
    start = int(start)
    end = int(end)
    # loop over de ID's
    for i in range(start,end+1):
        j = str(i)
        length = len(j)
        # maak valid hypothese :)
        valid = True
        # loop over alle lengtes 
        for k in reversed(range(1,int(length/2 +1))):
            # print(j,k)
            # als die splitsbaar is volgend de stapgroote dan
            if length % k == 0:
                # string splitsen op basis van stapgrootte
                k2 =  [j[m:m + k] for m in range(0, length, k)]
                # als alle items gelijk zijn aan elkaar dan is de id invalid
                if (all(item == k2[0] for item in k2)):
                    valid = False
        # Als hypothese verworpen is dan toevoegen aan lijst van invalid ids
        if valid == False:
            invalid.append(int(j))
answer2 = sum(invalid)
print(answer2)

