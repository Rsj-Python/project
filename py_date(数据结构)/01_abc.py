# 如果a + b + c = 1000，且a^2 + b^2 = c^2(a,b,c为自然数)，如何求出所有a,b,c可能的组合？
from time import *
begin = time()
for a in range(0,1001):
    for b in range(0,1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print('a,b,c:%d, %d, %d'%(a,b,c))
end = time()
print('time:%d'%(end - begin))