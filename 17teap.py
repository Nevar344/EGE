# a = [int(x) for x in open("17.txt")]
# ans = []
# k32 = len([x for x in a if x%32 == 0])
# for x,y in zip(a,a[1:]):
#     if (x<0 or y < 0) and x + y < k32:
#         ans.append(x+y)
# print(len(ans), max(ans))