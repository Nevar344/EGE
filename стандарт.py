def f(s,m):
    if s>=50: return m%2==0  #менять 50 на свое число, m не трогать
    if m==0: return 0         #не трогать
    h = [f(s+1,m-1), f(s*3,m-1)]  #менять s+1 и s*3 на ходы из задачи
    # пример если ходы +2, +4, x2: h = [f(s+2,m-1), f(s+4,m-1), f(s*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)  #не трогать

print('19',[s for s in range(1,50) if f(s,2)])               #менять только 50
print('20',[s for s in range(1,50) if not f(s,1) and f(s,3)])#менять только 50
print('21',[s for s in range(1,50) if not f(s,2) and f(s,4)])#менять только 50
