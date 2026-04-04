# from sys import* #можно юзать всегда
# setrecursionlimit(3000)
# def f(n):
#     if n == 1: return n
#     if n > 1:
#         return (n-1) * f(n-1)
# d = (f(2024)+2*f(2023))//f(2022)
# print(d)

# def F(n):
#     if n == 0: return 1
#     if n == 1: return 3
#     if n == 2: return 2
#     if n > 2: return F(n-1) * F(n-3)
# print(F(7))

# def F(n):
#     if n <= 3: return n
#     if n > 3 and n % 3 == 0:
#         return n**3+F(n-1)
#     if n > 3 and n%3 == 1:
#         return 4 + F(n//3)
#     if n > 3 and n % 3 == 2:
#         return n**2+F(n-2)
# print(F(100))

# def F(n):
#     if n <= 10: return n
#     if 10<n<=36:
#         return n // 4 + F(n-10)
#     if n > 36:
#         return 2 * F(n-5)
# print(F(100))

# def F(n):
#     if n == 1: return 2
#     if n > 1: return F(n-1)+5*n**2
# print(F(39))

# def F(n):
#     if n < 5: return 1 + 2*n
#     if n >=5 and n % 3 == 0: return 2 * (n+1)*F(n-2)
#     if n >=5 and n % 3 != 3: return 2 * n + 1 + F(n-1)+2*F(n-2)
# print(F(15))

# def F(n):
#     if n<= 1: return 1
#     if n > 1 and n%2 == 0:
#         return 3*n*F(n-1)
#     if n > 1 and n%2!=0:
#         return 2 * F(n-2)
# print(F(31))

# def F(n):
#     if n <= 3: return 3
#     if n%2==0 and n>3: return F(n//2)+5
#     if n%2!=0 and n>3: return F(n-1)-F(n-2)
# print(F(20))

# def F(n): #Если присутсвует квадратные скобки это значит, что это обычное деление и не надо пугаться
#     if n == 1: return 1
#     if n == 2: return 2
#     if n > 2 and n%2 == 0:
#         return (n+F(n-2)) // 5
#     if n > 2 and n%2!=0:
#         return (2*n+F(n-1)+F(n-2))//4
# print(F(50))

# def F(n):
#     if n <= 1: return 0
#     if n>1 and n%2!=0:
#         return F(n-1)+3*n**2
#     if n>1 and n%2==0:
#         return n//2 + F(n-1)+2
# print(F(49))

# from functools import lru_cache #Это если мы видем необычное строение такое как в этом примере, что сначало 0 это 1, а 1 это 3 тоесть вытекает с 1 на другой
# @lru_cache
# def F(n):
#     if n == 0: return 1
#     if n == 1: return 3
#     if n > 1:
#         return F(n-1)-F(n-2)+3*n
# for n in range(1,3000): #Обязательно условие при использовании кеширования (если не находится то пишем больше 3к)
#     F(n)
# print(F(40))

#ПРОТОТИП КОГДА НУЖНО НАЙТИ КОЛИЧЕСТВО Н НА ОТРЕЗКЕ

# def F(n):
#     if n <=18:
#         return n+3
#     if n > 18 and n%3==0:
#         return (n//3)*F(n//3)+n-12
#     if n>18 and n%3!=0:
#         return F(n-1)+n**2+5
# k = 0
# for i in range(1,1001):
#     x = F(i)
#     if all(int(d)%2==0 for d in str(x)): #Условие для нахождения четных чисел н
#         k+=1
# print(k)

# def F(n):
#     if n > 30: return n**2+5*n+4
#     if n <=30 and n%2 == 0:
#         return F(n+1)+3*F(n+4)
#     if n <=30 and n%2!=0:
#         return 2*F(n+2)+F(n+5)
# k = 0
# for i in range(1,1000):
#     x = F(i)
#     if sum(int(d) for d in str(x)) == 27: #Улсвоие когда сумма цифр должна быть ровно 27
#         k+=1
# print(k)

# def F(n):
#     if n == 0: return 0
#     if  n > 0 and n %2 == 0:
#         return F(n//2)
#     if n > 0 and n %2!=0:
#         return 1+F(n-1)
# k = 0
# for i in range(1,501): 
#     if F(i) == 8: #Условие что из 1 до 500 включительно те числа которые F(n)=8
#         k+= 1
# print(k)

# def F(n):
#     if n == 1: return 1
#     if n % 2 == 0:
#         return F(n//2)+1
#     else:
#         return F(n-1)+n
# m = []
# for i in range(1,1000):
#     if F(i) == 19:
#         m.append(i) #Создаем пустой список в который будем добавлять все значения н при котором выводится 19
# print(min(m))

# from sys import* #можно юзать всегда
# setrecursionlimit(3000)
# def F(n):
#     if n == 1: return n
#     if n >1: return n * F(n-1)
# d = (F(2024)-5*F(2023))//F(2022)
# print(d)

#Search Program "N"
# from functools import lru_cache
# @lru_cache(None)
# def F(n):
#     if n == 0: return n
#     if n>0 and n%2==0: return F(n/2) - 1
#     if n>0 and n%2!=0: return 1 + F(n-1)
# for n in range(4000):
#     F(n)
# k = 0
# for i in range(1000):
#     if F(i) == 0:
#         k+=1
# print(k)

# #Задача где дана картинка снизу
# # def F(n):
# #     print("*")
# #     if n > 1:
# #         F(n-2)
# #         F(n//2)
# #         print("*")
# #     print("*")
# #Решение этой задачи снизу
# def F(n):
#     k = 2
#     if n > 1:
#         k += F(n-2) + F(n//2) + 1
#     return k
# print(F(127))

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n < 100: return n**2
#     if n > 99 and n%2==0: return f(n-1)//2
#     if n > 99 and n%2!=0: return 2 * f(n-1)
# for n in range(1, 20000): #увеличиваем при необходимости
#     f(n)
# print((1000 * f(16384))/f(7777))

# from functools import lru_cache
# @lru_cache(None)
# def F(n):
#     if n < 15: return 4
#     if n >=15 and n%3==0: return F(2*n//3)+n-1
#     if n >=15 and n%3!=0: return F(n-1)+3
# for n in range(1, 1000):
#     F(n)
# for i in range(1, 1000):
#     if F(i) == 251:
#         print(i)

#Протатип где есть  F(n) и G(n)
# from functools import lru_cache
# def f(n):
#     return g(n-1)
# @lru_cache(None)
# def g(n):
#     if n <= 9: return 3*n
#     if n>9: return g(n-2)+1
# for i in range(1, 50000):
#     g(i)
# print(f(47995))

# from functools import lru_cache
# def F(n):
#     return G(n-1)+G(n-3)
# @lru_cache(None)
# def G(n):
#     if n <=9: return 3*n
#     if n > 9: return G(n-4)+2
# for i in range(1, 50000):
#     G(i)
# print(F(42999))

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n >=19: return f(n-4)+3580
#     if n < 19: return 6 * (g(n-7)-36)
# @lru_cache(None)
# def g(n):
#     if n >=248045: return n/20 + 28
#     if n < 248045: return g(n+9)-4

# for i in range(250000, 1, -1):
#     g(i)
# print(f(673))

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n >=7000: return n
#     if n < 7000: return f(n+2)+n+3
# for i in range(10000, 1, -1):
#     f(i)
# d = f(52)-f(56)
# print(d)

#Найти G(n) тогда используем sys
# import sys
# sys.setrecursionlimit(3000)
# def f(n):
#     if n <=2:return n #Заметим в условии что F(n)=G(n)=n значит в функции F(n)==n и то же самое и в G(n)==n только напишем в рекурсии для G(n)
#     if n >2: return g(n)+f(n-2)
# def g(n):
#     if n <=2:return n #Вот то самое G(n)==n как и говорили в стркое 113
#     if n > 2: return f(n-1)-g(n-2)
# print(g(15))

# import sys
# sys.setrecursionlimit(5000)
# def f(n):
#     if n >=3210: return 1
#     if n<3210: return f(n+3)+7
# def g(n):
#     if n <10: return n
#     if n >=10: return g(n-3)+5
# print(f(15)-g(3000))

#Найти N который равен 25
# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n<=2 or n == 8: return 0
#     if n == 3: return 1
#     if n >3 and n!=8: return f(n-2)+f(n-1)
# for i in range(1,10000):
#     f(i)
# for n in range(1,10000):
#     if f(n)==25:
#         print(n)
