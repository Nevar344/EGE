from itertools import *

def f(x,y,w,z):                  #менять: переменные из задачи
    return ((y<=x)or((not z) and w))==(w==x)  #менять: формула из задачи

for a in product([0,1],repeat=3):  #менять: repeat=сколько пустых ячеек в таблице
    table = [(a[0],1,0,0),(0,0,0,1),(0,1,a[1],a[2])]
    #менять: строки таблицы, вместо пустых ячеек пишешь a[0], a[1], a[2]...
    if len(table)==len(set(table)):  #не трогать — проверяет что строки не повторяются
        for p in permutations('xywz'):  #менять: буквы переменных
            if [f(**dict(zip(p,r))) for r in table]==[1,1,1]:  #менять: значения F
                print(p)