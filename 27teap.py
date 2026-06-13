#Певрое задание на кластеры пункт А
# from math import dist
# cl2 = [] #Кластер номер 2
# cl1 = [] #Кластер номер 1
# for i in open('27'): #Чистейший шаблон как и нижий
#     x, y = [float(j) for j in i.split()]
#     if y < 3: cl1.append([x, y]) #Шаблон но изменяется только число (чтобы понять какое там число нужно зайти вексель/либр и выделить все и нажать на вставку ив ыбрать диограмму а там выбрать разброс ХУ и найти где разделаются эти 2 кучи)
#     if y > 3: cl2.append([x, y]) #Шаблон но изменяется только число (чтобы понять какое там число нужно зайти вексель/либр и выделить все и нажать на вставку ив ыбрать диограмму а там выбрать разброс ХУ и найти где разделаются эти 2 кучи)

# def center(cl): #Функция для подчета центра определенного кластера
#     mn = []
#     for point1 in cl: # берем 1 точку из кластера
#         s = sum(dist(point1, point2) for point2 in cl) #подчет дистанции от 1 до 2 точки (считает сумму растояний до point1)
#         mn.append([s, point1]) # Заносим в список сначало  сумму а потом точку
#     return min(mn)[-1] #Нам нужна точка а не сумма поэтому мы берем point1
# x1, y1 = center(cl1)#Нашли кординаты центра 1 кластера
# x2, y2 = center(cl2)#Нашли кординаты центра 2 кластера
# Px = (x1 + x2) / 2 #Нашли среднее арефметические абцисс (х)
# Py = (y1 + y2) / 2 #Нашли среднее арефметические ординат (у)
# print("Ответ Для пункта А:", int(Px*10000), int(Py*10000)) #Смотрим на условие нас просят найти Px и Py умноженные на 10.000

#Певрое задание на кластеры пункт Б
# from math import dist
# cl3 = [] #Кластер номер 3
# cl2 = [] #Кластер номер 2
# cl1 = [] #Кластер номер 1
# for i in open('27'): #Чистейший шаблон как и нижий
#     x, y = [float(j) for j in i.split()]
#     if y < 3: cl1.append([x, y]) #Шаблон но изменяется только число (чтобы понять какое там число нужно зайти вексель/либр и выделить все и нажать на вставку ив ыбрать диограмму а там выбрать разброс ХУ и найти где разделаются эти 3 кучи)
#     if 3 < y < 7: cl2.append([x, y]) #Шаблон но изменяется только число (чтобы понять какое там число нужно зайти вексель/либр и выделить все и нажать на вставку ив ыбрать диограмму а там выбрать разброс ХУ и найти где разделаются эти 3 кучи)
#     if y > 7: cl3.append([x, y]) #Шаблон но изменяется только число (чтобы понять какое там число нужно зайти вексель/либр и выделить все и нажать на вставку ив ыбрать диограмму а там выбрать разброс ХУ и найти где разделаются эти 3 кучи)

# def center(cl): #Функция для подчета центра определенного кластера
#     mn = []
#     for point1 in cl: # берем 1 точку из кластера
#         s = sum(dist(point1, point2) for point2 in cl) #подчет дистанции от 1 до 2 точки (считает сумму растояний до point1)
#         mn.append([s, point1]) # Заносим в список сначало  сумму а потом точку
#     return min(mn)[-1] #Нам нужна точка а не сумма поэтому мы берем point1

# x1, y1 = center(cl1)#Нашли кординаты центра 1 кластера
# x2, y2 = center(cl2)#Нашли кординаты центра 2 кластера
# x3, y3 = center(cl3)#Нашли кординаты центра 3 кластера
# Px = (x1 + x2 + x3) / 3 #Нашли среднее арефметические абцисс (х)
# Py = (y1 + y2 + y3) / 3 #Нашли среднее арефметические ординат (у)
# print("Ответ Для пункта Б:", int(Px*10000), int(Py*10000)) #Смотрим на условие нас просят найти Px и Py умноженные на 10.000


#ЗАДАНИЕ ЗАДАЧА 2 НОМЕР 27
#Пункт А
# from math import dist
# data = [] #Место для точек с всего файла
# for i in open('27'):
#     x, y = [float(j) for j in i.replace(',', '.').split()]
#     data.append([x, y])

# #ЕСЛИ У НАС КАКИЕ ТО КОНЧЕННЫЕ КЛАССТЕРЫ ТАМ КРУГИ И ВСЯ ХУЙНЯ ПОДЗАБОРНАЯ ДЕЛАЕМ ЭТУ ШНЯГУ
# classters = [] #Автоматом находим точки 1 кластера и второго кластера
# while len(data) != 0: #Пока коллисетво точек не равно 0 мы будем ебашить класетры
#     classters.append([data.pop(0)]) #Добавляю кластер с 1 точкой (зародыш)
#     for p in classters[-1]:#Беру эту точку и нахожу соседей меньше 1
#         sosedi = [p1 for p1 in data if dist(p, p1) < 1] #Беру эту точку и нахожу соседей меньше 1 (Иногда в задаче написанно (можно играться с этим расстоянием (если есть выкидышь) если выкидышь имеется увеличиваем коэфицент там на 2 3 как хотите))
#         classters[-1] += sosedi
#         for p1 in sosedi: data.remove(p1)

# #Надо найти Кординаты центра каждого кластера. Px максимальное из абцисс центрового кластера и Py максимальное из ординат центрового кластера
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s, p1])
#     return min(mn)[1]#Как хочешь можешь -1 или 1 главное не 0

# cl1 = classters[0] #Берем из Автомата (дб скана) 0 из списка кластеров что является кординатой для кластера 1
# cl2 = classters[1] #Берем из Автомата (дб скана) 1 из списка кластеров что является кординатой для кластера 2
# x1, y1 = center(cl1)
# x2, y2 = center(cl2)
# Px = max(x1, x2)#По условию задачи нам надо макс от х1 и х2
# Py = max(y1, y2)#По условию надо макс от у1 и у2
# #В ОТВЕТЕ НАС ПРОСЯТ АБСОЛЮТНОЕ ЧИСЛО ЗНАЧИТ ОНО ДОЛЖНО БЫТЬ ПОД МОДУЛЕМ И ПРОСЯТ ЦЕЛОЕ ЗНАЧИТ INT
# print(int(Px * 10000), int(Py * 10000))

#ПУНКТ Б
#ТУТ НАМ ГОВОРЯТ ЧТО ЕСТЬ 3 ПОДКИДЫША (точки) И ОНИ ЕЩЕ И АНОМАЛЬНЫЕ

# from math import dist
# data = [] #Место для точек с всего файла
# for i in open('27'):
#     x, y = [float(j) for j in i.replace(',', '.').split()]
#     data.append([x, y])

# #ЕСЛИ У НАС КАКИЕ ТО КОНЧЕННЫЕ КЛАССТЕРЫ ТАМ КРУГИ И ВСЯ ХУЙНЯ ПОДЗАБОРНАЯ ДЕЛАЕМ ЭТУ ШНЯГУ
# classters = [] #Автоматом находим точки 1 кластера и второго кластера
# while len(data) != 0: #Пока коллисетво точек не равно 0 мы будем ебашить класетры
#     classters.append([data.pop(0)]) #Добавляю кластер с 1 точкой (зародыш)
#     for p in classters[-1]:#Беру эту точку и нахожу соседей меньше 1
#         sosedi = [p1 for p1 in data if dist(p, p1) < 1] #Беру эту точку и нахожу соседей меньше 1 (Иногда в задаче написанно (можно играться с этим расстоянием (если есть выкидышь) если выкидышь имеется увеличиваем коэфицент там на 2 3 как хотите))
#         classters[-1] += sosedi
#         for p1 in sosedi: data.remove(p1)
#     if len(classters[-1]) == 1: #Благодаря этой строчке мы можем понять что есть 3 слоняры и 3 подкидыша по 1 очку
#         classters.remove(classters[-1]) #Тут мы удаляем этих не нужных подкидышей
# cl1 = classters[0] #Говорим что в 1 класстере столько то точек (0 потому что у нас идет подсчет с 0 и первый будет 1)
# cl2 = classters[1] #Говорим что в 2 класстере столько то точек
# cl3 = classters[2] #Говорим что в 3 класстере столько то точек
# print('COUNT_T:', len(cl1), len(cl2), len(cl3))
# #Надо найти Кординаты центра каждого кластера. Px максимальное из абцисс центрового кластера и Py максимальное из ординат центрового кластера
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s, p1])
#     return min(mn)[1]#Как хочешь можешь -1 или 1 главное не 0

# #Почему мы взяли только 2 класстера потому что нас спрашивают разность максимально с минимальным поэтому мы заранее посмотрели скольок в каждем класстере
# x1, y1 = center(cl1)
# x3, y3 = center(cl3)
# Qx = (x1-x3)
# Qy = (y1-y3)
# #ТК У НАС АБСОЛЮТНОЕ ПРОСЯТ И ЦЕЛУЮ ЧАСТЬ МЫ УБИРАЕМ МИНУСЫ
# print(int(Qx*10000), int(Qy*10000))

#Решение задач

# from math import dist

# base = '' #Будем пихать в строку все
# files = ('27_A', '27_B')
# eps = (1, 2)

# for t in (0, 1):
#     data = [tuple(map(float, line.replace(',', '.').split()))
#             for line in open(base + files[t])]
#     clusters = []
#     while data:
#         clusters.append([data.pop()])
#         for p in clusters[-1]:
#             neigh = [pt for pt in data if dist(p, pt) < eps[0]]
#             clusters[-1] += neigh
#             for pt in neigh:
#                 data.remove(pt)
#     print(len(clusters), [len(c) for c in clusters])
#     clusters.sort(key=lambda c: len(c))
#     centers = []
#     for cl in clusters:
#         c = []
#         d_min = float('inf')
#         for p in cl:
#             d = sum(dist(p, pt) for pt in cl)
#             if d < d_min:
#                 d_min = d
#                 c = p
#         centers.append(c)
#     if t == 0:
#         A1 = min(len(c) for c in clusters)
#         A2 = sum(dist(c, (-1.0, 1.3)) for c in centers) #т.к в условии было ограничение от центра до (-1.0: 1.3)
#         print(A1, int(A2 * 10_000))
#     else:
#         B1 = sum(dist(p, centers[1]) < 1.6 for p in clusters[1]) - 1 #Условие что находится не более 1.6 от центра НЕ ВКЛЮЧАЯ ЦЕНТР
#         B2 = max(dist(centers[2], p) for p in clusters[2])
#         print(B1, int(B2 * 10_000))
#Условие этой задачи:
#𝐴1 — минимальное количество точек в кластере
#𝐴2— сумму расстояний от центров кластеров до точки с координатами (−1,0; 1,3)
#𝐵1— число точек, находящихся на расстоянии не более 1,6 от центра, не включая центр, в кластере со средним количеством точек
#𝐵2— максимальное расстояние от центра кластера с наибольшим количеством точек до другой точки этого кластера

#Задача 2

# from math import dist

# base = ''
# files = ['27_A', '27_B']
# eps = 1

# for t in (0, 1):
#     data = [tuple(map(float, line.replace(',', '.').split())) for line in open(base + files[t])]
#     clusters = []

#     while data:
#         clusters.append([data.pop(0)])
#         for p in clusters[-1]:
#             neigh = [pt for pt in data if dist(p, pt) < eps]
#             clusters[-1] += neigh
#             for pt in neigh:
#                 data.remove(pt)

#     clusters.sort(key=lambda cl: len(cl))
#     #print(len(clusters), [len(cl) for cl in clusters])

#     centers = []
#     for cl in clusters:
#         dmin = float('inf')
#         c = cl[0]
#         for p in cl:
#             d = sum(dist(p, pt) for pt in cl)
#             if d < dmin:
#                 dmin = d
#                 c = p
#         centers.append(c)
#     if t == 0:
#         p12 = [dist(p, (1.0, 1.)) for p in centers] #минимальное расстояние от точки с координатами (1,0; 1,0) до центра кластера
#         print(int(min(p12) * 10_000), int(max(p12) * 10_000)) #максимальное расстояние от этой же точки до центра кластера
#         #Тк расстояние одинаковое нет нужды перписывать одну формулу много раз легче в ответе написать минимум и максимум что и просят
#     else:
#         q12 = (len([p for p in clusters[-1] if dist(p, centers[-1]) < 1.2]), #наибольшим количеством точек число таких точек, которые находятся на расстоянии не более 1,2 от центра кластера
#                len([p for p in clusters[-1] if dist(p, centers[-1]) < 0.75])) #наибольшим количеством точек число таких точек, которые находятся на расстоянии не более 0,75 от центра кластера
#         print(q12[0], q12[1]) #Вывели 1 случай и 2 случай тоже чтобы много не писать сделали в 1 действие
#Условие этой задачи:
#P1 — минимальное расстояние от точки с координатами (1,0; 1,0) до центра кластера
#P2— максимальное расстояние от этой же точки до центра кластера
#Q1—  в кластере с наибольшим количеством точек число таких точек, которые находятся на расстоянии не более 1,2 от центра кластера
#Q2— в кластере с наибольшим количеством точек число таких точек, которые находятся на расстоянии не более 0,75 от центра кластера

#Задача номер 3

# from math import dist

# base = ''
# files = ['27_A', '27_B']
# eps = [1.5, 1]

# for t in (0, 1):
#     data = [tuple(map(float, line.replace(',', '.').split())) for line in open(base + files[t])]
#     clusters = []

#     while data:
#         clusters.append([data.pop(0)])
#         for p in clusters[-1]:
#             neigh = [pt for pt in data if dist(p, pt) < eps[t]]
#             clusters[-1] += neigh
#             for pt in neigh:
#                 data.remove(pt)
#     if t == 0:
#         clusters.sort(key=len)
#     #print(len(clusters), [len(c) for c in clusters])

#     centers = []
#     for cl in clusters:
#         dmin = float('inf')
#         c = [0, 0]
#         for p in cl:
#             d = min([dist(p, pt) for pt in cl])
#             if d < dmin:
#                 dmin = d
#                 c = p
#         centers.append(c)
#     #print(centers)
#     if t == 0:
#         p1 = len([p for p in clusters[1] if dist(p, centers[1]) <= 0.7])
#         p2 = len([p for p in clusters[0] if dist(p, centers[0]) > 1.3])
#         print(p1, p2)
#     else:
#         p0 = (1.7, 2.3)
#         q1 = min(dist(p0, p) for p in centers)
#         q2 = max(dist(p0, p) for p in centers)
#         print(int(10_000 * q1), int(10_000 * q2))

#Новый тип 27 задачи (цвета и тд) Повезло что нет нанамалий и всякий выкидышей
#Изначально смотрим на какие части разделяются наши кластеры в файле А и Б

cla = [[], []] #Заведем кластеры
for s in open('27_A'):
    s = s.replace(',', '.')
    x,y,har = s.split() #Разделим кластеры на х у и характеристику
    x,y = float(x), float(y) #Сразу переведем их в флоат формат
    col,svet,r = har[0], har[1], har[2:] #говорим что для цвета подходит 1 характеристика потому что цвет использует только один символ и остальные также
    if y > 10: cla[0].append([x,y,col,svet,r]) #Заранее мы посмотрели как по y они разделяются и вносим все хаарктеристики
    else: cla[1].append([x,y,col,svet,r])

clb = [[], [], []] #Заведем кластеры
for s in open('27_B'):
    s = s.replace(',', '.')
    x,y,har = s.split() #Разделим кластеры на х у и характеристику
    x,y = float(x), float(y) #Сразу переведем их в флоат формат
    col,svet,r = har[0], har[1], har[2:] #говорим что для цвета подходит 1 характеристика потому что цвет использует только один символ и остальные также
    if x > 22: clb[0].append([x,y,col,svet,r]) #Заранее мы посмотрели как по y они разделяются и вносим все хаарктеристики
    elif y > 22: clb[1].append([x,y,col,svet,r]) #Пишем услвоие так чтобы куча неподошедшая нам валялась в елсе
    else: clb[2].append([x,y,col,svet,r])

#Классчическая функция нахождения центроидов кроме 285 строки
from math import*
def center(cl):
    minsum = 10**9
    best = []
    for p in cl:
        summa = sum(dist(p[:2], p1[:2]) for p1 in cl) #Тут мы говорим что мы берем первые 2 значения тк другие уже характеристики
        if summa < minsum:
            minsum = summa
            best = p
    return best

#А1-мин расстояние от центра кластера с наименьшим колличсетвом точек до красного гиганта
#А2-максимальное расстояние от центра кл с наименьшим колво точек до крастного гиганта
cla.sort(key=len) #для того чтобы понять в каком кластере наименьшее колво точек
cent = center(cla[0])
sky = cla[0] + cla[1] #это во всех звездах
a1 = min(dist(cent[:2], [x, y]) for x,y,col,svet,r in sky if col+r=='YIII')*10000 #cent[:2] тк надо взять первые 2 услвие на А1
a2 = max(dist(cent[:2], [x, y]) for x,y,col,svet,r in sky if col+r=='YIII')*10000 #Условие на А2 (условие что цвет и размер будут равны Y и III по услвоию
print(int(a1), int(a2)) #Ответ на А 4940 74302

#Б1-мин растояние между двумя различными желтыми сверхгигантами распаложенными в одном и том же кластере
#Б2-расстояние между центрами кластеров с минимальным и максимальным колво желтых сверхгигантов
b1 = 10**9 #нам не нужен центр  поэтому берем что то большое
for cl in clb: #перебигаем по кластерам
    for x1,y1,col1,svet1,r1 in cl: #и внутри каждого кластера пробегаемся по точкам первую платнету
        for x2, y2, col2, svet2, r2 in cl: #это мы перебираем вторую платнету
            if not(x1==x2 and y1==y2) and col1+r1 == col2+r2 == 'ZI': #говорим что точки разные и это разные планеты и цвет и размер первой планеты и второй планеты равны ZI желтой сверхгигант и I размера
                b1 = min(b1, dist([x1,y1],[x2,y2])) #Находим растояние между нашими взятыми точками
for cl in clb: #Проверка на в каком кластере свехгигантов желтых
    print(len([1 for x,y,col,svet,r in cl if col+r=='ZI'])) #Перебираем звезды  и ищем те которые подходят (вместо единицы что угодно)
    #9, 3, 1 - Вывод. Получем что в 0 Кластере 9 штук что является максимальным / в 1 класстере 3 что не подходит к условию / в 2 кластере 1 что является минимальным
#Нужны 0, 2 кластеры
b2 = dist(center(clb[0])[:2], center(clb[2])[:2]) #дистанция от центроида 0 клстера к 2 центроиду кластер
print(int(b1*10000), int(b2*10000)) #1035 125591

#Без дб сканов
#1 задание
# from math import dist
# cl1 = []
# cl2 = []
# for i in open('27_A'):
#     x, y = [float(g) for g in i.replace(',', '.').split()]
#     if y < 3: #изначально посмотрел в ексель
#         cl1.append([x,y])
#     if y > 3:
#         cl2.append([x,y])
#
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl) #берем точку и сравниваем со всеми остальными точками и так мы суммируем эти расстояния
#         mn.append([s,p1]) #сначало расстояние потом сама точка
#     return min(mn)[1] #нашли центр нашего 1 кластера
# #Решение пункта А
# x1, y1 = center(cl1)
# x2, y2 = center(cl2)
# Px = (x1 + x2) / 2 #Среднее арефметич
# Py = (y1 + y2) / 2
# print('Ответ А:', int(Px * 10000), int(Py * 10000))

#Клатсерилизация
# from math import dist
# cl1 = []
# cl2 = []
# cl3 = []
# for i in open('27_B'):
#     x, y = [float(j) for j in i.split()]
#     if y < 4: cl1.append([x,y])
#     if 4 < y < 7: cl2.append([x,y])
#     if y > 7: cl3.append([x, y])
#
# #Поиск центра
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s, p1])
#     return min(mn)[1]
#
# #Услвоие для пункта Б
# x1, y1 = center(cl1)
# x2, y2 = center(cl2)
# x3, y3 = center(cl3)
# Px = (x1 + x2 + x3) / 3
# Py = (y1 + y2 + y3) / 3
#
# print(int(Px * 10_000), int(Py * 10_000))

#2 Задание
# from math import dist
# cl1 = []
# cl2 = []
# for i in open('27_A'):
#     x, y = [float(g) for g in i.replace(',', '.').split()]
#     if y < 15: cl1.append([x,y])
#     if y > 15: cl2.append([x, y])
#
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s,p1])
#     return min(mn)[1]
#
# x1, y1 = center(cl1)
# x2, y2 = center(cl2)
# Px = max(x1, x2) #Условие на максимальный из абцисс
# Py = max(y1, y2) #услвоие на макс из ординат
# print(int(Px * 10_000), int(Py * 10_000))
#Пункт Б
# from math import dist
# cl1 = []
# cl2 = []
# cl3 = []
# for i in open('27_B'):
#     x, y = [float(j) for j in i.split()]
#     if 5 < x < 20 and 0 < y < 10: cl1.append([x, y])
#     if 5 < x < 15 and 10 < y < 22: cl2.append([x, y])
#     if 5 < x < 15 and 22 < y < 30: cl3.append([x, y])
#
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s,p1])
#     return min(mn)[1]
#
# # print(len(cl1), len(cl2), len(cl3)) так мы смотрим какой из кластеров макс и мин и отсюда ищем те которые нужны
# #cl1 - 397, cl2 - 131, cl3 = 75
# x1, y1 = center(cl1)
# x3, y3 = center(cl3)
# Qx = abs(x1 - x3)
# Qy = abs(y1 - y3)
# print(int(Qx * 10_000), int(Qy * 10_000))

#Задание 2 пункт А

# from math import dist
# cl1 = []
# cl2 = []
# for i in open('27_A'):
#     x, y = [float(g) for g in i.replace(',', '.').split()]
#     if y < 15: cl1.append([x,y])
#     if y > 15: cl2.append([x, y])
#
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s,p1])
#     return min(mn)[1]
#
# x1, y1 = center(cl1)
# x2, y2 = center(cl2)
# Px = abs(x1 + x2) #Условие на максимальный из абцисс
# Py = abs(y1 + y2) #услвоие на макс из ординат
# print(int(Px * 10_000), int(Py * 10_000))

# #Пункт Б

# from math import dist
# cl1 = []
# cl2 = []
# cl3 = []
# for i in open('27_B'):
#     x, y = [float(g) for g in i.replace(',', '.').split()]
#     if 0 < x < 10: cl1.append([x,y])
#     if 12 < x < 19: cl2.append([x, y])
#     if 19 < x < 25: cl3.append([x, y])
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s,p1])
#     return min(mn)[1]
#
# # print(len(cl1), len(cl2), len(cl3)) посмотрел просто так
#
# p1 = center(cl1)
# p2 = center(cl2)
# p3 = center(cl3)
# d1 = dist(p1, p2)
# d2 = dist(p1, p3)
# d3 = dist(p2, p3)
# Q1 = min(d1, d2, d3) #минимальное расстояние между центрами
# Q2 = max(d1, d2, d3) #Максимальное расстояние между центрами
# print(int(Q1*10_000), int(Q2*10_000))

# #Пункт Б другого протатипа

# from math import dist
# cl1 = []
# cl2 = []
# cl3 = []
# for i in open('27_B'):
#     x, y = [float(g) for g in i.replace(',', '.').split()]
#     if -30 < x < -10 and -50 < y < -30: cl1.append([x,y])
#     if -10 < x < 10 and -50 < y < -20: cl2.append([x, y])
#     if -50 < x < -30: cl3.append([x, y])
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s,p1])
#     return min(mn)[1]
#
# p1 = center(cl1)
# p2 = center(cl2)
# p3 = center(cl3)
# start = [0, 0]
# d1 = dist(p1, start)
# d2 = dist(p2, start)
# d3 = dist(p3, start)
# Q1 = min(d1, d2 ,d3) #минимальное расстояние от центра ДО НАЧАЛА кординат
# Q2 = max(d1, d2, d3) #Максимальное расстояние от центра ДО НАЧАЛА кординат
# print(int(Q1*10_000), int(Q2*10_000))

# Пункт А Задча 6 хард

# from math import dist
# cl1 = []
# cl2 = []
# for i in open('27_A'):
#     x, y = [float(g) for g in i.replace(',', '.').split()]
#     if y < 15: cl1.append([x,y])
#     if y > 15: cl2.append([x, y])
#
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s,p1])
#     return min(mn)[1]
#
# # print(len(cl1), len(cl2))
# # 1)301 2)344
# x1, y1 = center(cl1)
# x2, y2 = center(cl2)
# A1 = len([1 for x, y in cl2 if y < y2]) #Услвоие на то что в кластере с наиб колво точек число точек ордината которых менбше ординаты центра
# A2 = abs(x1 - x2) # Условие что расстояние по очи абцисс между центрами кластеров
# print(A1, int(A2*10_000))

#Файл Б

# from math import dist
# cl1 = []
# cl2 = []
# cl3 = []
# for i in open('27_B'):
#     x, y = [float(g) for g in i.replace(',', '.').split()]
#     if 25 < y < 35: cl1.append([x,y])
#     if 18 < x < 23 and 10 < y < 20: cl2.append([x, y])
#     if 25 < x < 30: cl3.append([x, y])
#
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s,p1])
#     return min(mn)[1]
# # print(len(cl1), len(cl2), len(cl3)) 902 200 148 посомтрели наименьший кластер для задачи
#
# x3, y3 = center(cl3)
# B1 = len([1 for x, y in cl3 if x3 - 0.9 < x < x3 + 0.9 and y3 - 0.9 < y < y3 + 0.9])
# print(B1) #Условие что число точек наименьшего по колво точек кластера находящихсч ВНУТРИ квадрата с центром в центре этого кластера сторонами и длинной 1.8
# #поэтому радиус этого квадрата равен 1.8 /2 = 0.9
# x2, y2 = center(cl2)
# x1, y1 = center(cl1)
# B2 = abs(y2- y1) #Условие что расстояние по оси ординат между центрами кластеров с наибольшим и средним колво точек
# print(int(B2*10_000))

#Практика
#Px​ — среднее арифметическое абсцисс центров кластеров, и PyPy​ — среднее арифметическое ординат центров кластеров. В ответе запишите четыре числа: в первой строке сначала целую часть произведения Px×10000Px​×10000, затем целую часть произведения Py×10000Py​×10000 для файла A, во второй строке — аналогичные данные для файла B.
# from math import dist
# def solve(filename, num_clusters):
#     data = []
#     for i in open(filename):
#         x, y = [float(j) for j in i.split()]
#         data.append([x, y])
#     # Кластеризация (BFS-расширение)
#     clasters = []
#     while len(data) != 0:
#         clasters.append([data.pop(0)])
#         for p1 in clasters[-1]:
#             sosedi = [p2 for p2 in data if dist(p1, p2) < 0.4]
#             clasters[-1] += sosedi
#             for p2 in sosedi: data.remove(p2)
#     # Центроид: точка с минимальной суммой расстояний (истинный центр)
#     def centroid(cl):
#         mn = []
#         for p1 in cl:
#             s = sum(dist(p1, p2) for p2 in cl)
#             mn.append([s, p1])
#         return min(mn)[1]
#     # Берём num_clusters крупнейших кластеров
#     clasters.sort(key=len, reverse=True)
#     centers = [centroid(cl) for cl in clasters[:num_clusters]]
#     Px = sum(x for x, y in centers) / len(centers)
#     Py = sum(y for x, y in centers) / len(centers)
#     print(int(Px * 10000), int(Py * 10000))


#С характеристиками
#Пункт А (найти кординатуцентра каждого кластера а затем 2 числа абциссу и ординату красного ближайщего гиганта
# cl1 = []
# cl2 = []
# red = []
# for i in open('27_A'):
#     x, y, type = i.replace(',', '.').split()
#     x, y = float(x), float(y)
#     if type[0] == 'M' and type[2:] == 'III': red.append([x,y])#отдельн особираем гигнтов красных
#     #проводим кластерилизацию
#     if y < 15: cl1.append([x,y])
#     if y > 15: cl2.append([x,y])
# # print(len(cl1), len(cl2)) #114 121 отсюда вывод что наименьшее колво точек в 1 кластере (нужно для задания
# from math import dist
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1,p2) for p2 in cl)
#         mn.append([s, p1])
#     return min(mn)[1]
#
# p1 = center(cl1)
# mn = []
# for pr in red:
#     s = dist(p1, pr)
#     mn.append([s, pr])
# Ax, Ay = min(mn)[1]
# print(int(Ax*10_000), int(Ay*10_000))
#Пункт Б (Найти расстояние между центрами кластеров с наименьшим и наибольшим колво оранжевых гигантов/В2- наибольшее расстофние между желтыми карликами одного кластера)

# y1, y2, y3 = [], [], []
# o1, o2, o3 = [], [], []
# cl1, cl2, cl3 = [], [], []
# for i in open('27_B'):
#     x, y, type = i.replace(',', '.').split()
#     x, y = float(x), float(y)
#     if y < 30:
#         cl1.append([x, y])
#         if type[0] == 'K' and type[2:] == 'III': o1.append([x, y])
#         if type[0] == 'G' and type[2:] == 'V': y1.append([x, y])
#
#     if y > 30 and x < 16:
#         cl2.append([x, y])
#         if type[0] == 'K' and type[2:] == 'III': o2.append([x, y])
#         if type[0] == 'G' and type[2:] == 'V': y2.append([x, y])
#
#     if x > 16:
#         cl3.append([x, y])
#         if type[0] == 'K' and type[2:] == 'III': o3.append([x, y])
#         if type[0] == 'G' and type[2:] == 'V': y3.append([x, y])
#
# from math import dist
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s, p1])
#     return min(mn)[1]
#
# # print(len(o1), len(o2), len(o3)) 87 28 25 Проверили в каждом кластере сколько желтых
# B1 = dist(center(cl1), center(cl3)) #максимальный с мин дистанция нужна по условию
# #Поиск наибольшего расстояние между желтыми карликами одного кластера снизу показано как мы пробегаемся по всем карликам в каждом кластере и в конце мы соединяем все списки и находим максимальный
# r1 = [dist(a,b) for a in y1 for b in y1 if a != b]
# r2 = [dist(a,b) for a in y2 for b in y2 if a != b]
# r3 = [dist(a,b) for a in y3 for b in y3 if a != b]
# B2 = max(r1+r2+r3)
#
# print(int(B1*10_000), int(B2*10_000))

#Задание 2 (А)
#Мин расстояние от центра кластера д обелого карлика из этого же кластера  и тоже самое для максимального
# cl1 = []
# cl2 = []
# w1, w2 = [], []
# for i in open('27_A'):
#     x, y, type = i.replace(',', '.').split()
#     x, y = float(x), float(y)
#     #проводим кластерилизацию
#     if y < 9:
#         cl1.append([x,y])
#         if type == 'VII': w1.append([x,y])
#     if y > 9:
#         cl2.append([x,y])
#         if type == 'VII': w2.append([x, y])
# from math import dist
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s, p1])
#     return min(mn)[1]
# p1 =center(cl1)
# p2 = center(cl2)
# r1 = [dist(p1,p) for p in w1 if p1 != p]
# r2 = [dist(p2,p) for p in w2 if p2 != p]
# r = r1+r2
# A1 =min (r)
# A2 = max(r)
# print(int(A1*10_000), int(A2*10_000))

#Пункт Б
#Мин расстояние между двумя звездами с подклассом не менее 8 расположеных в разных кластерах/В2 - среднее расстояние между двумя различн звездами с подклассом не менее 8 в одном кластере
# cl1 = []
# cl2 = []
# cl3 = []
# v1, v2, v3 = [], [], []
# for i in open('27_B'):
#     x, y, type = i.replace(',', '.').split()
#     x, y = float(x), float(y)
#     #проводим кластерилизацию
#     if y < 15:
#         cl1.append([x,y])
#         if type[1] in ['8', '9']: v1.append([x,y])
#     if 15 < y < 20:
#         cl2.append([x, y])
#         if type[1] in ['8', '9']: v2.append([x, y])
#     if y > 21:
#         cl3.append([x, y])
#         if type[1] in ['8', '9']: v3.append([x, y])
#
# from math import dist
# r1 = [dist(a ,b) for a in v1 for b in v2] #Смотрим все звезды в разных клатерах
# r2 = [dist(a ,b) for a in v2 for b in v3]
# r3 = [dist(a ,b) for a in v1 for b in v3]
# B1 = min(r1+r2+r3)
#
# z1 = [dist(a,b) for a in v1 for b in v1 if a != b]
# z2 = [dist(a,b) for a in v2 for b in v2 if a != b]
# z3 = [dist(a,b) for a in v3 for b in v3 if a != b]
# z = z1 + z2 + z3
# B2 = sum(z) / len(z)
# print(int(B1*10_000), int(B2*10_000))

#Задание 3 (А)

# cl1, cl2 = [], []
# s3 = []
# for i in open('27_A'):
#     x, y, type = i.replace(',', '.').split()
#     x, y = float(x), float(y)
#     #проводим кластерилизацию
#     if y < 9:
#         cl1.append([x,y])
#     if y > 9:
#         cl2.append([x,y])
#     if type[:2] == 'L3': s3.append([x,y])
# from math import dist
# def center(cl):
#     mn = []
#     for p1 in cl:
#         s = sum(dist(p1, p2) for p2 in cl)
#         mn.append([s, p1])
#     return min(mn)[1] #Если просят АНТИЦЕНТР или КРАЙ то меняем на макс
# # print(len(cl1), len(cl2)) 131 92
# p2 = center(cl2)
# A1 = max([dist(p2,p) for p in s3]) #Наиб расстояние от центра кластера с наименьшим колво точек до синей звезды
# p1 = center(cl1)
# A2 = max([dist(p1, p) for p in s3])#Наиб расстояние от центра с наибольшим колво точек до синей звезды
# print(int(A1*10_000), int(A2*10_000))
