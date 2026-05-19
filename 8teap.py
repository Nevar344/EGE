# from itertools import*
# cnt = 0
# for x in product(sorted("ФОКУС"), repeat = 5):
#     s = "".join(x)
#     cnt += 1
#     if s.count("Ф") == 0 and s.count("У") == 2:
#         print(cnt)

#Чередования

# from itertools import* #условие что 2 четные и 2 нечетные не стоят рядом
# k = 0
# for x in product("012345", repeat = 5):
#     s = "".join(x)
#     if s[0] != "0": #Проверяется для всех где есть числа
#         s = s.replace("2", "0").replace("4", "0")
#         s = s.replace("3", "1").replace("5", "1")
#         if "11" not in s and "00" not in s:
#             k += 1
# print(k)

# from itertools import*
# k = 0
# for x in product("01234567", repeat = 5):
#     s = "".join(x)
#     if s[0] != "0":
#         s = s.replace("3", "1").replace("5", "1").replace("7", "1")
#         if "16" not in s and "61" not in s and s.count("6")==1:
#             k += 1
# print(k)

# from itertools import*
# k = 0
# for x in set(permutations("АББАТИСА")): #т.к говорят что каждая буква встречается столько сколько в заданном слове значит permutations
#     s = "".join(x)
#     s = s.replace("А", "1").replace("И", "1")
#     s = s.replace("Б", "2").replace("Т", "2").replace("С", "2")
#     if "11" not in s and "22" not in s:
#         k+=1
# print(k)

# from itertools import*
# k = 0
# for x in product("2121Ш1222", repeat = 5): #заменил гласные и согласные на цифры (сразу)
#     s = "".join(x)
#     if s.count("1") > s.count("2") + s.count("Ш") and "1Ш" not in s and "Ш1" not in s:
#         k+=1 # из за того что Ш мы не написали как 2 мы прибавим count("Ш")
# print(k)

#Хард задание

# from itertools import*
# k = 0
# for x in permutations("ХЛЕБНЫЙМЯКИШ", r = 7):
#     s = "".join(x)
#     if s[0]=="Х" and x[3] in "БЫКИШ":
#         for c in "ЛБНЙМКШ": s = s.replace(c, "Х")
#         if "ХХ" not in s:
#             k+=1
# print(k)

#ПОД КАКИМ НОМЕРОМ ИДЕТ СЛОВО В КОТОРОМ БУКВА А НЕ СТОИТ РЯДОМ С Л, Е и одна буква повторяется а остальные различны
# from itertools import*
# cnt = 0
# for x in product(sorted('АПРЕЛЬ'), repeat = 6):
#     s = ''.join(x)
#     cnt += 1
#     g = [s.count(j) for j in s] #Проверка на повторение
#     if (not 'АЛ' in s) and (not 'ЕА' in s) and (not 'ЛА' in s) and (not 'АЕ' in s) and ((g.count(2)==2) and (g.count(1)==4)):
#         print(cnt)
#         break

#Под каким номером в списке идет первое слово в котором две буквы М
# from itertools import*
# cnt = 0
# for x in product(sorted('ЛЮМИКС'), repeat= 6):
#     s = ''.join(x)
#     cnt += 1
#     if 'ММ' in s:
#         print(cnt)
#         break

#ОПРЕДЕЛИ ПОД КАКИМ НОМЕРОМ ИДЕТ ПЕРВОЕ СЛОВО С "НУБАС"
# from itertools import*
# cnt = 0
# for x in product(sorted('НУБАС'), repeat = 5):
#     s = ''.join(x)
#     cnt += 1
#     if s == 'НУБАС':
#         print(cnt)
#         break

#Под каким номером в списке идет слово начинающее на П и заканчивающее на Ш
# from itertools import*
# cnt = 0
# for x in product(sorted('ШЛЯПА'), repeat = 6):
#     s = ''.join(x)
#     cnt += 1
#     if s[0] == "П" and s[-1] == "Ш":
#         print(cnt)
#         break

#УКАЖИТЕ КОЛЛИЧЕСТВО СЛОВ КОТОРЫЕ СТОЯТ МЕЖДУ СЛОВАМИ ИНАФФ и НФАИА (включая их)
# from itertools import*
# cnt = 0
# for x in product(sorted('ИНФА'), repeat = 5):
#     s = ''.join(x)
#     cnt += 1
#     if 'ИНАФФ' <= s <= 'НФАИА':
#         print(cnt)
# print('ОТвет',709-400+1) #ТАК КАК МЫ ВКЛЮЧАЕМ ПОЭТОМУ +1

#СОздает С ПЕРЕСТАНОВКОЙ когда одинаковые буквы не могут стоять рядом друг с другом
# from itertools import*
# cnt = set()
# for x in permutations('КАПКАН'):
#     s = ''.join(x)
#     if not 'КК' in s and not 'АА' in s:
#         print(s)
#         cnt.add(s)
# print(len(cnt))

#Сколько существует чисел при которых все цифры различны и никакие 2 нечетные и 2 четные не стоят рядом
# from itertools import*
# cnt = 0
# for x in permutations("01234567"):
#     s = ''.join(x)
#     g = [int(s[j]) % 2 != int(s[j+1]) % 2 for j in range(len(s)-1)]
#     if (s[0] != '0') and all(g):
#         print(s)
#         cnt+=1
# print(cnt)

#Сколько РАЗЛИЧНЫХ кодов можно сделеать чтобы были 3 гласные подрят
# from itertools import*
# c = set() #чтобы не было всяких повторов
# gl = "ОА" #сюда выписали все возможные гласные
# for x in permutations('ОБОРОНА'): #пермутейшн т.к различные
#     s = ''.join(x)
#     g = [s[j] in gl and s[j+1] in gl and s[j+2] in gl for j in range(len(s)-2)] #проверка на 3 гласные подрят
#     if any(g): #условие
#         print(s)
#         c.add(s)
# print(len(c))

# #Каждая буква встречается 1 раз при этом согласные не могут быть рядом и буква И не должна быть первой и буква О не должна быть последеней
# from itertools import*
# cnt = set()
# sl = 'СЛВ'
# for x in permutations('УСЛОВИЕ'):
#     s = ''.join(x)
#     g = [ s[j] in sl and s[j+1] in sl for j in range(len(s)-1) ]
#     if (not any(g)) and s[0] != 'И' and s[-1] != 'О':
#         print(s)
#         cnt.add(s)
# print(len(cnt))

#Найти сколько слов когда слово может иметь длинну от 3 до 6 букв (включительно
# from itertools import*
# cnt = set()
# for g in range(3, 7):
#     for x in product(sorted('РАСЧЁСКА'), repeat = g):
#         s = ''.join(x)
#         cnt.add(s)
# print(len(cnt))
