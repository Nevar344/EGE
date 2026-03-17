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

