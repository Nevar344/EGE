# from ipaddress import*
# k = 0
# net = ip_network("172.16.192.0/255.255.192.0", 0)
# for ip in net:
#     b = f"{int(ip):032b}"
#     if b.count("1") % 5 != 0:
#         k += 1
# print(k)

# from ipaddress import*
# net = ip_network("145.92.137.88/255.255.240.0", 0)
# print(net) #поиск айпи адресса

# from ipaddress import*
# for mask in range(32): #Перебор маски
#     net1 = ip_network(f"220.128.112.142/{mask}", 0)
#     net2 = ip_network(f"220.128.96.0/{mask}", 0)
#     if net1 == net2:
#         print(net1, net1.netmask) #Сначало смотрим вывод net1  замечаем, что айпи адресс схож и данным в тексте и смотрим какая маска стоит у него и оттуда отлакиваемся и берем 3 байт (3 символ с лева на право)

# from ipaddress import*
# for mask in range(32):
#     net1 = ip_network(f"115.127.30.120/{mask}", 0)
#     net2 = ip_network(f"115.127.151.120/{mask}", 0)
#     if net1 == net2:
#         print(net1, net1.netmask) #Заметим что по условию нам требуется найти 3 байт слева но все 3 символы равны 0 значит 0

# from ipaddress import*
# for mask in range(32):
#     net1 = ip_network(f"111.81.208.27/{mask}", 0)
#     net2 = ip_network(f"111.81.192.0/{mask}", 0)
#     if net1 == net2:
#         print(net1, net1.netmask) #Т.к нам требуется найти минимальный байт то мы смотрим на схожесть net1 и замечаем что их 2 и выбираем наименьший во 2 столбце

# from ipaddress import*
# for mask in range(32):
#     net1 = ip_network(f"115.12.69.38/{mask}", 0)
#     net2 = ip_network(f"115.12.64.0/{mask}", 0)
#     if net1 == net2:
#         print(net1, net1.netmask) #Вывод 18 т.к есть 4 схожих адресса и среди них справа есть цифры например 0/18 значит там 18 единиц то есть нам подходит этот ответ т.к это наименьший

# from ipaddress import*
# for mask in range(32):
#     net1 = ip_network(f"93.138.164.49/{mask}", 0)
#     net2 = ip_network(f"93.138.160.0/{mask}", 0)
#     if net1 == net2:
#         print(net1, net1.netmask) #просят найти сколько различных значений поэтому смотрим одинаковые net1 которые похожи на net2 и пишем коллво масок у них

#Поиск номера пк!

# from ipaddress import *
# # Создаем объект сети
# net = ip_network("162.198.0.157/255.255.255.224", 0)
# # Номер компьютера в сети (индекс хоста)
# host_number = int(ip_address("162.198.0.157")) - int(net.network_address)
# print(host_number)

# from ipaddress import*
# net = ip_network("162.198.75.44/255.255.240.0", 0)
# host_number = int(ip_address("162.198.75.44")) - int(net.network_address)
# print(host_number)

# from ipaddress import* # Сколько в этой сети IP-адресов, для которых количество единиц в их двоичной записи кратно 2?
# k = 0
# net = ip_network("172.16.160.0/255.255.240.0", 0)
# for ip in net:
#     b = f"{int(ip):032b}"
#     if b.count("1")%2==0:
#         k+=1
# print(k)

# from ipaddress import*
# net =ip_network("190.202.83.62/255.255.252.0", 0) #Найдите наибольший IP-адрес в данной сети, который может быть назначен компьютеру. В ответе укажите сумму числовых значений октетов найденного IP-адреса.
# print(net[-2], 190+202+83+254)

# from ipaddress import*
# net = ip_network("46.29.170.214/255.255.128.0", 0) #Найдите в данной сети наибольший IP-адрес, который может быть назначен компьютеру, при условии, что значение одного из октетов IP-адреса является суммой его остальных октетов
# for ip in net.hosts():
#     a = [int(x) for x in str(ip).split(".")] #генератор с учетом удаления точек
#     x, y, z, w = a
#     if (x == z+y+w) or (y==x+z+w) or (w==x+z+y): 
#         print(ip) #нужен наибольний поэтому последний 

# from ipaddress import*
# net = ip_network("111.222.0.124/255.255.224.0", 0)
# for ip in net:
#     b = f"{int(ip):032b}"
#     if (b.count("0") * b.count("1"))%2 != 0: #Найдите в данной сети наибольший IP-адрес, у которого произведение количества нулей и количества единиц в двоичной записи IP-адреса явялется нечётным числом.
#         print(ip, 111+222+31+255)

# from ipaddress import* #Найдите в данной сети наибольший IP-адрес, который содержит два октета с нечётным значением и может быть назначен компьютеру.
# net = ip_network("202.71.92.91/255.255.192.0", 0)
# for ip in net.hosts():
#     a = [int(x) for x in str(ip).split(".")]
#     x, y, z, w = a
#     if (x and y) % 2 !=0 or (y and z) % 2!=0 or (z and w) % 2 !=0:
#         print(ip, "20271127254")

# from ipaddress import* #Найдите наибольший в данной сети IP-адрес, в котором одинаковое количество нулей и единиц в двоичной записи.
# net = ip_network("192.168.12.207/255.192.0.0", 0)
# for ip in net:
#     b = f"{int(ip):032b}"
#     if b.count("0") == b.count("1"):
#         print(ip, 1921912540)

# from ipaddress import* #Найдите наименьший в данной сети IP-адрес, в котором количество единиц в двоичной записи кратно 5.
# net = ip_network("172.95.116.174/255.255.192.0", 0)
# for ip in net:
#     b = f"{int(ip):032b}"
#     if b.count("1") % 5 == 0:
#         print(ip, 172+95+64+15)
#         break #тк наименьший

# from ipaddress import*
# net = ip_network("172.95.116.174/255.255.192.0", 0)
# for ip in net.hosts(): #айдите наименьший в данной сети IP-адрес, который может быть назначен компьютеру.
#     print(ip)
#     break
# print("Ответ:", 172+95+64+1)

# from ipaddress import *
# for mask in range(33): #Определите минимальное количество единиц в разрядах маски, если известно, что у наибольшего IP-адреса устройства в данной сети в двоичной записи содержится ровно 19 единиц.
#     net = ip_network(f'84.32.84.32/{mask}', 0)
#     if f'{net[-2]:b}'.count('1') == 19: 
#         print(mask)
#         break
