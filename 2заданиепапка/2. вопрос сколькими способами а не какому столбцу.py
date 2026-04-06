from itertools import *
def f(x,y,w,z):                  #менять: переменные из задачи
    return (x and (y<=z)) or w   #менять: формула из задачи
d = set()
for a1,a2,a3,a4,a5,a6 in product([0,1],repeat=6):  #менять: repeat=сколько пустых ячеек
    t = [(1,0,a1,1),(a2,0,1,a3),(a4,0,a5,a6)]      #менять: строки таблицы, пустые = a1,a2...
    if len(t)==len(set(t)):                          #не трогать
        for p in permutations('xywz'):               #менять: буквы переменных
            if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:  #менять: значения F
                d.add(p)
print(len(d))  #выводит количество способов

#ЭТОТ ШАБЛОН — когда вопрос "сколькими способами"