# #Найти длинну самой длинной подцепочки латинского алфавита не содержащий гласных букв
# f = open('24')
# s = f.readline()
# s = s.replace('E', 'A') #Заменили все гдасные на 1 гласную А для удобства
# s1 = s.split('A')
# mx = -1000000000000000002
# for i in s1:
#     if len(i) > mx:
#         mx = len(i)
# print(mx)

# Найти самую длинную подцепочку состоящей из символов ACD
# f = open('24')
# s = f.readline()
# l = lmax = 0
# for i in range(len(s)): #проходимся по элементам
#     if s[i] in 'ACD': #говорим что нужно ACD
#         l += 1
#         if l > lmax: #Проверка на максимум (если она является максимальной просто переписываем ее
#             lmax = l
#     else:
#         l = 0
# print(lmax)

#Определить длинну макс послежовательности идущих символов где соседи различны
# f = open('24')
# s = f.readline()
# l = lmax = 0
# for i in range(len(s)-1): #-1 тк надо проверить еще и последний сивол на пару
#     if s[i] != s[i + 1]:
#         l += 1
#         if l > lmax:
#             lmax = l
#     else:
#         l = 0
# print(lmax+1) #Тк 30 строка находит только колво пар а символов всегда на 1 больше

# Найти макс колво пар подрят символов RE или RA искомая может включать только пары ра или содержать одновременно ра и ре
# f = open('24')
# s = f.readline()
# s = s.replace('RE', "RA") #Заменили для удобства
# for i in range(len(s)+10): #перещитываем с запасом (на самом деле это очень сильно нагрузит пк лучше поделить на 2)
#     if 'RA' * i in s:
#         print(i) #нас просили пары поэтому ответ такой же как и на выводе (ЕСЛИ БЫ ПРОСИЛИ ЭЛЕМНЕНТЫ ТО ТОГДА НАДО БЫЛО БЫ УМНОЖИТЬ НА 2 (RA или RE)

#С ИЗЮМЕНКОЙ
#Определить макс длинну ПОДСТРОКИ! состоящей из RSO иои OSR
#Заметим что они похожи и могут быть в одной тсроке записаны как OSR и RSO и тогда они не будут перечитываться как в прошлый раз
#ТРОЙКИ НЕ МОГУТ ПЕРЕСЕКАТЬСЯ
# f = open('24')
# s = f.readline()
# s = s.replace('OSRSO', 'OSR RSO')#Заменили чтобы избавиться от не удовлетворяющегося случая
# s = s.replace('RSOSR', 'RSO OSR')#Заменили чтобы избавиться от не удовлетворяющегося случая
# s = s.replace('OSR', 'RSO') #Заменили на более удобный формат
# for i in range(len(s)):
#     if 'RSO' * i in s: #провели проверку сколько раз оно повторяется в строке
#         print(i*3) #умножили на 3 так как нам требуют не пары троек а их элементы длинну (умножаем на колво букв в паре тоесть на 3)

#Определить макс колво идущих подрят символов среди которых нет EF
# f = open('24')
# s = f.readline()
# s = s.replace('EF', 'E F') #Для того чтобы правильно подсчитал длинну используем
# s1 = s.split()
# # mx = max(len(i) for i in s1) #альтернатива
# mx = max(map(len, s1)) #для поиска максимального колво идущих символов подрят
# print(mx)

#Двойные циклы (не надежный метод но тоже)
#
# s = open('1.txt').readline()
# #print(len(s)) 6500000
# maxx = 0
# for i in range(len(s)):
#     if i%100000==0: print(i)
#     for j in range(i + maxx, len(s)):
#         cut = s[i:j+1]
#         if cut.count('2025') >50: break
#         if cut.count('2025') == 50 and cut[-4:] == '2025' and cut.count('Y') >=140:
#             maxx = max(maxx, len(cut))
# print(maxx) #938

#Двойным Указателем
# s = open('1.txt').readline()
# l = maxx = ky = k2025 = 0
# for r in range(len(s)):
#     if s[r] == 'Y': ky += 1
#     if s[r-3:r+1] == '2025': k2025+=1 #От r мы делаем срез на 4 символа назад
#     while k2025>50:
#         if s[l:l+4] == '2025': k2025 -= 1
#         if s[l] == 'Y': ky -= 1
#         l+=1
#     if k2025==50 and ky>=140 and s[r-3:r+1] == '2025':
#         maxx = max(maxx, r-l+1)
# print(maxx)

#в файле минимальное колво символов
#20 встретиться ровно 26 раз
#Гласная буква встречается ровно один раз и заканчивается ею
# s = open('2.txt').readline()
# for c in "AEIOUQY": s = s.replace(c, 'A')
# minn = 10**9
# k20=ka=l=0
# for r in range(len(s)):
#     if s[r-1:r+1] == '20': k20+=1
#     if s[r] == 'A': ka += 1
#     while k20>26 or ka>1:
#         if s[l:l+2] == '20': k20 -= 1
#         if s[l] == 'A': ka -= 1
#         l += 1
#     if s[r] == 'A' and k20 == 26 and ka==1:
#         while s[l:l + 2] != '20' and s[l] != 'A':
#             l+=1
#         minn = min(minn, r-l+1)
# print(minn) #58

#Q, R, W и цифр 1, 2, 4.
#Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых ни одна буква не стоит рядом с буквой, а цифра – с цифрой.
# a = open('24').readline()
# mx = 0
#
# a = a.replace('R', 'Q').replace('W', 'Q')
# a = a.replace('2', '1').replace('4', '1')
#
# for l in range(len(a)):
#     for r in range(l + mx, len(a) + 1):
#         s = a[l:r]
#         if s.count('11') != s.count('QQ') or s.count('11') != 0 or s.count('QQ') != 0:
#             break
#         if s.count('11') == s.count('QQ'):
#             mx = max(len(s), mx)
#
# print(mx)

# Найдите максимальную длину подстроки, в которой символы a и d не стоят рядом
# a = open('24').readline()
# a = a.replace('ad', ' a d').replace('da', 'd a').split()
# mx = 0
# for s in a:
#     mx = max(mx, len(s))
# print(mx)

#Определите максимальное количество идущих подряд пар символов вида согласная + гласная
#A, B, C, D и O.
# a = open('24-2.txt').readline()
# for i in 'BCD': a = a.replace(i, 'B')
# for i in 'AO': a = a.replace(i, 'A')
# a = a.replace('BA', '*')
# a = a.replace('A', ' ').replace('B', ' ').split()
# mx = 0
# for s in a:
#     mx = max(mx, len(s))
# print(mx)

#Регулярки
#Определите максимальное количество подряд идущих последовательностей символов NPO или PNO в прилагаемом файл
#последовательность должна состоять только из троек NPO, или только из троек PNO, или только из троек NPO и PNO в произвольном порядке их следования.
# from re import *
# a = open('24-4.txt').readline()
# case = r'((NPO)|(PNO))+'
# mx = 0
# for i in finditer(case, a):
#     mx = max(len(i.group(0)), mx)
# print(mx // 3)

#Циклами Текстовый файл состоит из символов T, U, V, W, X, Y и Z
#Определите в прилагаемом файле максимальное количество идущих подряд символов (длину
# непрерывной подпоследовательности), среди которых символ Y встречается не более 150
# a = open('24-4.txt').readline()
# mx = 1
# for l in range((len(a))):
#     for r in range(l+mx, len(a)):
#         s = a[l: r+1]
#         if s.count('Y') > 150: break
#         if s.count('Y') <= 150: mx = max(mx, len(s))
# print(mx)

#файл состоит из символов, обозначающих заглавные буквы латинского алфавита и цифры от 1 до 9 включительно
#которые могут представлять запись числа в шестнадцатеричной
#Цифры, числовое значение которых превышает 9, обозначены латинскими
# from re import *
# a = open('24-5.txt').readline()
# case = r'[1-F][0-F]*'
# mx = 0
# for i in finditer(case, a):
#     mx = max(mx, len(i.group(0)))
# print(mx)

#файл состоит из символов T, U, V, W, X, Y и Z.
#среди которых символ T встречается ровно 100 раз
# a = open('24-6.txt').readline()
# mx = 0
# a = a.split('T')
# for i in range(len(a)-100):
#     s = 'T'.join(a[i:i+101])
#     mx = max(mx, len(s))
# print(mx)

#Текстовый файл состоит из символов A, B, C, D, E и F
#которых пара символов CD (в указанном порядке) встречается ровно 160 раз
# a = open('24-7.txt').readline()
# mx = 0
# a = a.replace('CD', 'C D').split()
# for i in range(len(a)-160):
#     s = ''.join(a[i:i+161])
#     mx = max(mx, len(s))
# print(mx)

#подряд символов, среди которых ровно 35 букв S, начинающуюся чётной цифрой не содержащую других чётных цифр, кроме первой
# a = open('24-8.txt').readline()
# mx = 0
# for i in '02468': a = a.replace(i, '0')
# a = a.split('0')
# for s in a:
#     while s.count('S') >= 35:
#         if s.count('S') == 35: mx = max(mx, len(s))
#         s = s[:-1]
# print(mx)

# среди которых ровно 35 букв Q, начинающуюся нечётной цифрой не содержащую других нечётных цифр, кроме первой
# a = open('24-9.txt').readline()
# mx = 1
# for i in '13579': a = a.replace(i, '1')
# for l in range(len(a)):
#     if a[l] in '1':
#         for r in range(l + mx, len(a)):
#             s = a[l:r+1]
#             if s.count('1') > 1 or s.count("Q") > 35: break
#             if s.count('1') == 1 and s.count("Q") == 35:
#                 mx = max(mx, len(s))
# print(mx)

#которых подстрока 2025 встречается не менее 90 раз и при этом содержится ровно 80 букв Y.
# a = open('24-10.txt').readline()
# mx = 1
# for l in range(len(a)):
#     for r in range(l + mx, len(a)):
#         s = a[l:r+1]
#         if s.count('Y') > 80: break
#         if s.count('2025') >= 90 and s.count('Y') == 80:
#             mx = max(mx, len(s))
# print(mx)

#подряд одинаковых букв, начинающуюся и заканчивающуюся чётной цифрой, не содержащую
#других букв, кроме повторяющихся, не содержащую цифр, кроме первой и последней
# a = open('24-11.txt').readline()
# for i in '02468': a = a.replace(i, '0')
#
# a = a.split('0')
# mx = 0
# for s in a:
#     if len(set(s)) == 1 and s[0] not in '13579':
#         mx = max(mx, len(s) + 2)
# print(mx)

#начинается и заканчивается одинаковой гласной буквой и не содержит букв внутри
# from re import *
# a = open('24-12.txt').readline()
# mx = 0
# for b in 'AEIOUY':
#     case = rf'[{b}][^A-Z]+[{b}]'
#     for i in finditer(case, a):
#         mx = max(len(i.group(0)), mx)
# print(mx)


# a = open('24-12.txt').readline()
# for i in '0123456789': a = a.replace(i, '0')
# mx = 0
#
# for l in range(len(a)):
#     if a[l] in 'AEIOUY':
#         c = 1
#         for r in range(l + 1, len(a)):
#             if a[r] == '0':
#                 c += 1
#             if a[r] != '0':
#                 if a[r] == a[l]:
#                     c += 1
#                     mx = max(mx, c)
#                 break
# print(mx)
