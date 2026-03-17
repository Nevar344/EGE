# def f(x):
#     return (x%a==0) or ((60<=x<=80)<=(x%22!=0))
# for a in range(1,10000):
#     if all(f(x)== 1 for x in range(1,1_000)):
#         print(a)
# def f(x):
#     return ((x%19!=0) or (x%15!=0))<=(x%a!=0)
# for a in range(1,1000):
#     if all(f(x)==1 for x in range(1,1000000)):
#         print(a)
# def f(x):
#     return ((x%12==0) <= (x%90!=0)) or (x+2*a>=512)
# for a in range(1,1000):
#     if all(f(x)==1 for x in range(1,1000000)):
#         print(a)
#         break
# def f(x):
#     return (x%a==0) or ((70<=x<=80) <= (x%18!=0))
# for a in range(1000, 1, -1):
#     if all(f(x)==1 for x in range(1,1000000)):
#         print(a)
#         break
# k = 0
# def f(x):
#     return (a%35==0) and ((730%x==0) <= ((a%x!=0)<= (110%x!=0)))
# for a in range(1,1001):
#     if all(f(x)==1 for x in range(1,1000000)):
#         k+=1
# print(k)
# def f(x):
#     return (x&29!= 0)<= ((x&12 == 0)<=(x&a!=0))
# for a in range(1,1000):
#     if all(f(x)==1 for x in range(1,1000000)):
#         print(a)
# def f(x):
#     return ((x&673!=0) or (x&189!=0)) <= (x& a > 0)
# for a in range(1,1000):
#     if all(f(x)==1 for x in range(1,1000000)):
#         print(a)
#         break

#Нахождение а,когда есть 2 или более переменные
#"Дел"" это (x%y==0)
#Отрицание лучше записывать через != внутри скобок

# def f(x, y):
#     return (x*y<3*a) or (x>=31) or (x<5*y)
# for a in range(1,1000):
#     if all(f(x, y) == 1 for x in range(1,1000) for y in range(1,1000)):
#         print(a)
#         break
# def f(x, y):
#     return (x+2*y>a) or (y<x) or (x<30)
# for a in range(1000,1, -1):
#     if all(f(x,y)==1 for x in range(0,1000) for y in range(0,1000)):
#         print(1,a)
#         break
# def f(x, y):
#     return (x>=27) or (2*x<3*y) or (a>(x+2)*(y-3))
# for a in range(1,1000):
#     if all(f(x, y)==1 for x in range(0,1000) for y in range(0,1000)):
#         print(2, a)
#         break

# def poz(n, m): #Функция для "ПОЗ" Нахождения разности
#     return n-m>0

# def f(x, y):
#     return not poz(x+y, 73) or not poz(37, x-y) or poz(y, a)
# for a in range(1000,1, -1):
#     if all(f(x,y)==1 for x in range(0,1000) for y in range(0,1000)):
#         print(a)
#         break

# def tr(n, m, k): # Функция для проверки ТРЕУГ
#     return n+m>k and n+k > m and m+k>n

# def f(x):
#     return tr(a, 7, x) <= ((max(x+5, 14)<=27) == (not tr(36,21,x)))
# for a in range(1000,1,-1):
#     if all(f(x)==1 for x in range(1,1000000)):
#         print(a)
#         break

#НАХОЖДЕНИЕ НЕИЗВЕСТНОГО ОТРЕЗКА

# def f(x):
#     P = x<=x<=20
#     Q = 15<=x<=25
#     A = a1<=x<=a2
#     return ((not A)<=(not P)) or Q
# ox = [dx for x in (2,15,20,25) for dx in (x,x+0.1,x-0.1)]
# m = []
# for a1 in ox:
#     for a2 in ox:
#         if a2>=a1 and all(f(x)==1 for x in ox):
#             m.append(a2-a1)
# print(min(m))

# def f(x):
#     P = 10<=x<=29 #указываем отрезки
#     Q = 13<=x<=18 #указываем отрезкти
#     A = a1<=x<=a2
#     return ((A)<=(P)) or (Q)
# ox = [dx for x in (10,13,29,18) for dx in (x, x+0.1,x-0.1)]
# m = []
# for a1 in ox:
#     for a2 in ox:
#         if a1<=a2 and all(f(x)==1 for x in ox):
#             m.append(a2-a1)
# print(max(m))

# def f(x):
#     P = 135<=x<=218
#     Q = 174<=x<=308
#     R = 246<=x<=382
#     A = a1<=x<=a2
#     return (not Q<=(P or R))<=((not A)<=(not Q))
# ox = [dx for x in (135, 174, 218, 246, 308, 382) for dx in (x, x+0.1,x-0.1)]
# m = []
# for a1 in ox:
#     for a2 in ox:
#         if a1<=a2 and all(f(x)== 1 for x in ox):
#             m.append(a2-a1)
# print(min(m))

# def f(x):
#     B = 36<=x<=75
#     C = 60<=x<=110
#     A = a1<=x<=a2
#     return (not A)<=((B) == (C))
# ox = [dx for x in (36, 60, 75, 110) for dx in (x, x+0.1,x-0.1)]
# m = []
# for a1 in ox:
#     for a2 in ox:
#         if a1<=a2 and all(f(x)==1 for x in ox):
#             m.append(a2-a1)
# print(min(m))

# def f(x):
#     P = 15<=x<=40
#     Q = 35<=x<=60
#     A = a1<=x<=a2
#     return ((not Q) or P) and A
# ox = [dx for x in (15,35,40,60) for dx in (x, x+0.1,x-0.1)]
# m = []
# for a1 in ox:
#     for a2 in ox:
#         if a1<=a2 and all(f(x)==0 for x in ox):
#             m.append(a2-a1)
# print(max(m)) 

#ТИП МНОЖЕСТВА ВЕРОЯТНОСТЬ ПОЧТИ НУЛЕВАЯ
# Нужно сначало создать пустое множество через a = set()
# и если при проверке через 
# for x in range(1,1000):
#    if f(x)==0:
#        print(x)
#выводяться цифры то приходим обратно к а и пишем те числа в множество которые у нас появились при проверке пример a = {6, 12, 18}
#ручной метод

# a = set() #Если просят минимальное множество
# def f(x):
#     P = x in {2,4,6,8,10,12,14,16,18,20}
#     Q = x in {3,6,9,12,15,18,21,24,27,30}
#     A = x in a
#     return (P<=A) or ((not A) <=(not Q))
# for x in range(1,1000):
#     if f(x)==0:
#         a.add(x)
# print(a) #метод автоматом без поиска ручным методом

# a = set(range(1,1000)) #Если просят максимальное множество
# def f(x):
#     P = x in {2,4,6,8,10,12,14,16,18,20}
#     Q = x in {5,10,15,20,25,30,35,40,45,50}
#     A = x in a
#     return (A<=P) or ((not Q)<=(not A))
# for x in range(1,1000):
#     if f(x)==0:
#         a.remove(x) #Убираем те значения которые нам не подходят
# print(len(a)) #Если просят длинну

# 1 способ решения множества (уровень сложный)

# from itertools import*
# zep = ["".join(x) for x in product('01', repeat = 8)]
# p = {x for x in zep if x[0]+x[1]=="11"}
# q = {x for x in zep if x[-1]=="0"}
# a =set()
# def f(x):
#     P = x in p
#     Q = x in q
#     A = x in a
#     return (not A)<=(P or (not Q))
# for x in zep:
#     if f(x)==0:
#         a.add(x)
# print(len(a))

# 2 способ решения множества (уровень сложный)

# from itertools import*
# a =set()
# def f(x):
#     P = x[0] + x[1] == "11"
#     Q = x[-1] == "0"
#     A = x in a
#     return (not A)<=(P or (not Q))
# for x in product("01", repeat = 8):
#     if f(x)==0:
#         a.add(x)
# print(len(a))

#Сложный тип делимость

# k = 0
# def f(x):
#     return (a%5==0) and (2020%a!=0)<=((x%1718==0)<=(2023%a==0))
# for a in range(1,10000):
#     if all(f(x)==1 for x in range(1,1000000)):
#         k+= 1
# print(k)

#Практика

# def f(x): # Del
#     return ((x%15==0) and (x%21!=0)) <= ((x%a!=0) or (x%15!=0))
# for a in range(1,1000):
#     if all(f(x)==1 for x in range(1,1000000)):
#         print(a)
#         break

# def f(x, y): #Defolt (2 symbol)
#     return (x*y>a) and (x>y) and (x<8)
# for a in range(1,1000):
#     if all(f(x, y)==0 for x in range(1,1000) for y in range(1,1000)):
#         print(a)
#         break

# def f(x, y): #Defolt (2 symbol)
#     return (x>39) or (y> 26) or (2*x+4*y<a)
# for a in range(1,1000):
#     if all(f(x, y)==1 for x in range(1,1000) for y in range(1,1000)):
#         print(a)
#         break

# def f(x, y): #Defolt (2 symbol)
#     return (2*x + y != 70) or (x<y) or (a<x)
# for a in range(1000,1,-1):
#     if all(f(x,y)==1 for x in range(0,1000) for y in range(0,1000)):
#         print(a)
#         break

# def f(x, y): #Defolt (2 symbol)
#     return (x**2-10*x+16>0) or (y**2-10*y+21>0) or (x*y<2*a)
# for a in range(1,1000):
#     if all(f(x, y)==1 for x in range(1,1000) for y in range(1,1000)):
#         print(a)
#         break

# m = [] #Отрезки
# def f(x):
#     P = 17<=x<=54
#     Q = 37<=x<=83
#     A = a1<=x<=a2
#     return P <= ((Q and (not A)) <= (not P))
# ox = [dx for x in (17,37,54,83) for dx in (x, x+0.1,x-0.1)]
# for a1 in ox:
#     for a2 in ox:
#         if a2>=a1 and all(f(x)==1 for x in ox):
#             m.append(a2-a1)
# print(min(m))

# m = [] #Отрезки
# def f(x):
#     B = 18<=x<=52
#     C = 16<=x<=41
#     A = a1<=x<=a2
#     return (B<=A) and ((not C) or A)
# ox = [dx for x in (16,18,41,52) for dx in (x,x+0.1,x-0,1)]
# for a1 in ox:
#     for a2 in ox:
#         if a2>=a1 and all(f(x)==1 for x in ox):
#             m.append(a2-a1)
# print(min(m))