file = open("input.txt","r")
content =file.read()
file.close()
code = content.split('\n')

#%% eindnummer
# number = 50
# for i in code[:-1]:
#     if i[0] == "R":
#         number += int(i[1:])
#     elif i[0] == "L":
#         number -= int(i[1:])
# print(number)
# if number < 0:
#     print(100-(abs(number) % 100))
# else:
#     print(abs(number) % 100)
#%%
# number = 50
# amountzero = 0
# for i in code[:-1]:
#     if i[0] == "R":
#         number += int(i[1:])
#     elif i[0] == "L":
#         number -= int(i[1:])
#     #print(number, abs(number) % 100, int(i[1:]))
#     if abs(number) % 100 == 0:
#         amountzero += 1
# print(amountzero)
#%%
# number = 1000050
# amountzero = 0
# code2 = [number]
# for i in code[:-1]:
#     if i[0] == "R":
#         number += int(i[1:])
#     elif i[0] == "L":
#         number -= int(i[1:])
#     code2.append(number) 
#     #print(number, abs(number) % 100, int(i[1:]))
#     if abs(number) % 100 == 0:
#         amountzero += 1
# print(amountzero)

# amountturned = 0
# for n in range(1,len(code2)):
#     old = code2[n-1]
#     new = code2[n]
#     oldhun = old - abs(old) % 100
#     newhun = new - abs(new) % 100
#     #verschil in hondertallen optellen
#     amountturned += abs(oldhun-newhun)/100
#     #edgecase
#     if(abs(old) % 100 == 0 and old>new):
#         amountturned -=1
#     if(abs(oldhun-newhun)/100 != 0 and)
#         amountturned -=1
#     # print(amountturned, abs(oldhun-newhun)/100,old,new)
#     if (abs(oldhun-newhun)/100 != 0):
#         print(n, oldhun, newhun, abs(old) % 100 == 0 and old>new, abs(new)% 100 == 0)
        
# total = amountzero + amountturned
# print(total)

#%%
# nummer hoog gezet om niet met negatieve getallen te hoeven dealen
number = 1000050
amountzero = 0
code2 = [number]
for i in code[:-1]:
    # rechts is optellen links is aftrekken
    if i[0] == "R":
        number += int(i[1:])
    elif i[0] == "L":
        number -= int(i[1:])
    # reeks opslaan
    code2.append(number) 
    #print(number, abs(number) % 100, int(i[1:]))
    # als 00 +1
    if abs(number) % 100 == 0:
        amountzero += 1
print(amountzero)


# rotaties bijhouden
amountturned = 0
for n in range(1,len(code2)):
    # elke stap vergelijken
    old = code2[n-1]
    new = code2[n]
    # hondertallen uit de nummers halen
    oldhun = old - abs(old) % 100
    newhun = new - abs(new) % 100
    #verschil in hondertallen checken
    if(abs(oldhun-newhun)/100 != 0):
        # als er verschil is maar oude nummer was 0 neem dan 1 stap minder als je naar links zou draaien
        if(abs(old) % 100 == 0 and new < old):
            amountturned -=1
        amountturned += abs(oldhun-newhun)/100
    # als je uitkomt op 0 en je naar links aan het draaien bent
    if (abs(new) % 100 == 0 and new < old):
        amountturned += 1
    # print(n, amountturned) 
print(amountturned)
