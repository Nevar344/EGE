# for n in range(1,1000):
#     b = bin(n)[2:]
#     if n % 2 == 0:
#         b = "10" + b
#     else:
#         b = "1" + b + "01"
#     R = int(b, 2)
#     if n <= 12:
#         print(R)

# for n in range(1,1000):
#     b = bin(n)[2:]
#     b = b+b[-1]
#     if b.count("1") % 2 == 0:
#         b = b + "0"
#     else:
#         b = b+"1"
#     if b.count("1") % 2 == 0:
#         b = b + "0"
#     else:
#         b = b+"1"
#     R = int(b, 2)
#     if R >130:
#         print(n)
#         break
    