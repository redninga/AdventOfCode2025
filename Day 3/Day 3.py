file = open("input.txt","r")
content =file.read()
file.close()
code = content.split('\n')

#%% part 1
numbers = []
# loop over batches
for i in code:
    # batches omzetten in losse nummers
    ilist = list(i)
    ilist = [int(num) for num in ilist]
    # maximum van de lijst bepalen die niet de laatste nummer is
    maxi1 = max(ilist[:-1])
    n1index = ilist[:-1].index(maxi1)
    # nieuwe lijst aanmaken beginnend van het max en hier het max van pakken
    ilist2 = ilist[n1index+1:]
    maxi2 = max(ilist2)
    n2index = ilist2.index(maxi2)
    # nummers omzetten in goede eenheden
    numbers.append(maxi1 * 10 + maxi2)
print(sum(numbers))

#%% part 2

# functie voor recursie maken
def part2(ilist,n):
    # max halen uit de lijst min het aantal nummers rechts nog over moeten blijven
    maxi1 = max(ilist[:-n])
    n1index = ilist[:-n].index(maxi1)
    ilist2 = ilist[n1index+1:]
    # als laatste nummer gedaan moet worden doe dit met de hand
    if n == 1:
        maxi2 = max(ilist2)
        return (maxi1 * 10 + maxi2)
    else:
        # functie opnieuw aanroepen en nummer goed zetten in grootheid zetten
        return (10 ** n * maxi1 + part2(ilist2,n-1))

numbers = []
# loop over batches
for i in code:
    # batches omzetten in losse nummers
    ilist = list(i)
    ilist = [int(num) for num in ilist]
    # functie aanroepen
    numbers.append(part2(ilist, 11))

print(sum(numbers))


# invalid = []
# # loop over ranges
# for ids in code:
#     [start,end] = ids.split('-')
#     start = int(start)
#     end = int(end)
#     # loop over de ID's
#     for i in range(start,end+1):
#         j = str(i)
#         length = len(j)
#         # als ID een even lengte heeft dan vergelijk de 2 helften
#         if length % 2 == 0:
#             part1 = j[int(length/2):]
#             part2 = j[:int(length/2)]
#             if part1 == part2:
#                 invalid.append(int(j))
# answer1 = sum(invalid)
# print(answer1)

#%% part 1
# invalid = []
# # loop over ranges
# for ids in code:
#     [start,end] = ids.split('-')
#     start = int(start)
#     end = int(end)
#     # loop over de ID's
#     for i in range(start,end+1):
#         j = str(i)
#         length = len(j)
#         # maak valid hypothese :)
#         valid = True
#         # loop over alle lengtes 
#         for k in reversed(range(1,int(length/2 +1))):
#             # print(j,k)
#             # als die splitsbaar is volgend de stapgroote dan
#             if length % k == 0:
#                 # string splitsen op basis van stapgrootte
#                 k2 =  [j[m:m + k] for m in range(0, length, k)]
#                 # als alle items gelijk zijn aan elkaar dan is de id invalid
#                 if (all(item == k2[0] for item in k2)):
#                     valid = False
#         # Als hypothese verworpen is dan toevoegen aan lijst van invalid ids
#         if valid == False:
#             invalid.append(int(j))
# answer2 = sum(invalid)
# print(answer2)

