"""Написать скрипт решения квадратного уравнения"""

import math
a=int(input('input a ' ))
b=int(input('input b ' ))
c=int(input('input c ' ))
print(a, 'x^2+', b, 'x+', c, '=0', sep='')
D=b**2-4*a*c
print('D =', D)
if(D>0):
    x_1=(-b+math.sqrt(D))/2*a
    x_2=(-b-math.sqrt(D))/2*a
    print('x_1 =', x_1, 'x_2 =', x_2)
elif(D==0):
    x=(-b)/2*a
    print('x =', x)
else:
    print('D<0=korney net')

