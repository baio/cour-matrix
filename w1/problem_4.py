__author__ = 'baio'

from GF2 import one

a = [1, 1, 0, 0, 0, 0, 0]
b = [0, 1, 1, 0, 0, 0, 0]
c = [0, 0, 1, 1, 0, 0, 0]
d = [0, 0, 0, 1, 1, 0, 0]
e = [0, 0, 0, 0, 1, 1, 0]
f = [0, 0, 0, 0, 0, 1, 1]

u = [0, 0, 1, 0, 0, 1, 0]

c+d=[0, 0, 1, 0, 1, 0, 0]
1+e=[0, 0, 1, 0, 0, 1, 0] <= u

---------------------------

u = [0, 1, 0, 0, 0, 1, 0]

b+c=[0, 1, 0, 1, 0, 0, 0]
1+d=[0, 1, 0, 0, 1, 0, 0]
2+e=[0, 1, 0, 0, 0, 1, 0] <= u

****************************

a = [1, 1, 1, 0, 0, 0, 0]
b = [0, 1, 1, 1, 0, 0, 0]
c = [0, 0, 1, 1, 1, 0, 0]
d = [0, 0, 0, 1, 1, 1, 0]
e = [0, 0, 0, 0, 1, 1, 1]
f = [0, 0, 0, 0, 0, 1, 1]

u = [0, 0, 1, 0, 0, 1, 0]

c+d=[0, 0, 1, 0, 0, 1, 0] <= u

------------------------------
u = [0, 1, 0, 0, 0, 1, 0]

b+c=[0, 1, 0, 0, 1, 0, 0]
<= ?