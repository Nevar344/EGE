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
#     if s >=125: return "w"
#     if any(game(i)=="w" for i in moves(s)): return "p1"
#     if all(game(i)=="p1" for i in moves(s)): return "v1"
#     if any(game(i)=="v1" for i in moves(s)): return "p2"
#     if all(game(i) in ["p1", "p2"] for i in moves(s)): return "v2"
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
