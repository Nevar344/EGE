from itertools import *
def f(a,b,c,d):                    #менять: если 4 переменные к примеру xyzw — def f(x,y,z,w)
    return (a<=d) and (not(b<=c))      #менять: сюда формулу из задачи
    # туторчик:
    # x→y         пишется как: x<=y
    # ¬(x→y)      пишется как: not(x<=y)
    # x∧y         пишется как: x and y
    # ¬(x∧y)      пишется как: not(x and y)
    # x∨y         пишется как: x or y
    # ¬(x∨y)      пишется как: not(x or y)
    # ¬x          пишется как: not x
    # x≡y         пишется как: x==y
    # x⊕y (XOR)   пишется как: x!=y
    # x↓y (NOR)   пишется как: not(x or y)
    # x|y (NAND)  пишется как: not(x and y)
table = [(1,0,1,0),(1,1,1,0),(0,0,1,0)]        #менять: строки таблицы без столбца F
for p in permutations('abcd'):    #менять: 'xyz' если 3 переменные, 'xyzw' если 4
    if [f(**dict(zip(p,row))) for row in table]==[1,1,1]:  #менять: [0,1] — значения F из таблицы
        print(p)