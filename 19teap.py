# def f(s, m):
#     if s >= 51: return m%2 == 0
#     if m == 0: return 0
#     h = [f(s+1,m-1),f(s+4,m-1), f(s*2, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
# print(19, [s for s in range(1,51) if f(s,2)])
# print(20, [s for s in range(1,51) if not f(s,1) and f(s, 3)])
# print(21, [s for s in range(1,51) if not f(s,2) and f(s, 4)])

#Прграмма вадима
# from functools import*

# def moves(s):
#     return s+2, s+4, s*2
# @lru_cache(None)
# def game(s):
#     if s >=125: return "w" #услвоие победы
#     if any(game(i)=="w" for i in moves(s)): return "p1" #p1 это значит первый ход пети
#     if all(game(i)=="p1" for i in moves(s)): return "v1" #v1 Это Ваня и в этом условии проверяется что при ходе пети он одержит победу
#     if any(game(i)=="v1" for i in moves(s)): return "p2" #Это петя и при любом ходе вани он одержит победу
#     if all(game(i) in ["p1", "p2"] for i in moves(s)): return "v2" #Это 2 ход Вани при котором он одержит победу 
# print(19,[s for s in range(1,125) if game(s)=="v1"])
# print(20,[s for s in range(1,125) if game(s)=="p2"])
# print(21,[s for s in range(1,125) if game(s)=="v2"])

# from functools import*

# def moves(s):
#     return s+2, s+4, s*2
# @lru_cache(None)
# def game(s):
#     if s >=125: return 0
#     m = [game(i) for i in moves(s)]
#     m0 = [i for i in m if i % 2 == 0]
#     return min(m0)+1 if len(m0)>0 else max(m)+1
# print(19,[s for s in range(1,125) if game(s)==2])
# print(20,[s for s in range(1,125) if game(s)==3])
# print(21,[s for s in range(1,125) if game(s)==4])
#hello team

#ЕГКР
# from functools import*

# def moves(s):
#     return s+1, s+5, s*3
# @lru_cache(None)
# def game(s):
#     if s >=124: return "w" #услвоие победы
#     if any(game(i)=="w" for i in moves(s)): return "p1" #p1 это значит первый ход пети
#     if all(game(i)=="p1" for i in moves(s)): return "v1" #v1 Это Ваня и в этом условии проверяется что при ходе пети он одержит победу
#     if any(game(i)=="v1" for i in moves(s)): return "p2" #Это петя и при любом ходе вани он одержит победу
#     if all(game(i) in ["p1", "p2"] for i in moves(s)): return "v2" #Это 2 ход Вани при котором он одержит победу 
# print(19,[s for s in range(1,125) if game(s)=="v1"])
# print(20,[s for s in range(1,125) if game(s)=="p2"])
# print(21,[s for s in range(1,125) if game(s)=="v2"])


#Убывание
#19
# def F(k, x):
#     if k <= 11 and x == 3: return True
#     if k > 11 and x == 3: return False
#     if k <= 11: return False

#     if x % 2 == 0: #Ход ВАНИ!
#         return F(k-3, x+1) or F(k-7, x+1) or F(k // 3, x+1)
#     else:
#         return F(k-3, x+1) and F(k-7, x+1) and F(k // 3, x+1)
# for k in range(12, 1000):
#     if F(k, 1):
#         print(k) #36, 37, 38
#20
# def F(k, x):
#     if k <= 11 and x == 4: return True #4 это Петя
#     if k > 11 and x == 4: return False #4 это Петя 
#     if k <= 11: return False

#     if x % 2 == 1: #Ход ПЕТИ!
#         return F(k-3, x+1) or F(k-7, x+1) or F(k // 3, x+1)
#     else:
#         return F(k-3, x+1) and F(k-7, x+1) and F(k // 3, x+1)
# for k in range(12, 1000):
#     if F(k, 1):
#         print(k) #39, 40
#21
# def F(k, x):
#     if k <= 11 and (x == 3 or x == 5): return True
#     if k > 11 and x == 5: return False
#     if k <= 11: return False

#     if x % 2 == 0: #Ход Вани!
#         return F(k-3, x+1) or F(k-7, x+1) or F(k // 3, x+1)
#     else:
#         return F(k-3, x+1) and F(k-7, x+1) and F(k // 3, x+1)
# for k in range(12, 1000):
#     if F(k, 1):
#         print(k) #исключаем что получили в 19 задаче и смотрим что есть (42)

#Две кучи
# def F(k1, k2, x):
#     if x == 3 and (k1+k2) >=259: return True #3 это Ваня
#     if x == 3 and (k1+k2) < 259: return False
#     if (k1+k2) >= 259: return False

#     if x % 2 == 0:
#         return F(k1+1, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2+1, x+1) or F(k1, k2*2, x+1)
#     else:
#         return F(k1+1, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2+1, x+1) or F(k1, k2*2, x+1)
# for k2 in range(1,242):
#     if F(17, k2, 1):
#         print(k2)
#         #Когда ход неудачный тогда мы пишем везде or (61) только в 19 номере

#20
# def F(k1, k2, x):
#     if x == 4 and (k1+k2) >=259: return True #4 это Петя
#     if x == 4 and (k1+k2) < 259: return False
#     if (k1+k2) >= 259: return False
# #Петя не может выйграть за 1 ход
# #Петя может выйграть своим 2 ходом НЕЗАВИСИМО ОТ ХОДА ВАНИ
#     if x % 2 == 1:
#         return F(k1+1, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2+1, x+1) or F(k1, k2*2, x+1)
#     else:
#         return F(k1+1, k2, x + 1) and F(k1 * 2, k2, x + 1) and F(k1, k2+1, x+1) and F(k1, k2*2, x+1)
# for k2 in range(1,242):
#     if F(17, k2, 1):
#         print(k2)

#21
#У вани есть вайграшная страта в котором выйгрывает первым или вторым ходом при любом ходе Пети
#У вани нет стратегии которая гарантированная даст выйграть 1 ходом
# def F(k1, k2, x):#обязательно проверяем условия когда только х == 3 чтобы исключить вариант в котором он побеждает 1 ходом
#     if (x == 3 or x == 5) and (k1+k2) >=259: return True #3 это Ваня (ход 1) 5 это Ваня (ход 3)
#     if x == 5 and (k1+k2) < 259: return False
#     if (k1+k2) >= 259: return False
#     if x % 2 == 0:
#         return F(k1+1, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2+1, x+1) or F(k1, k2*2, x+1)
#     else:
#         return F(k1+1, k2, x + 1) and F(k1 * 2, k2, x + 1) and F(k1, k2+1, x+1) and F(k1, k2*2, x+1)
# for k2 in range(1,242):
#     if F(17, k2, 1):
#         print(k2) #111
