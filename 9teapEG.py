k = 0
for i in open("9"):
    a = [int(x) for x in i.split()]
    pov_3 = [x for x in i if i.count(x)== 3]
    pov_1 = [x for x in i if i.count(x)== 1]
    if len(pov_3) == 6 and len(pov_1) == 1:
        if pov_3[0] > pov_1[0]:
            k += 1
print(k)