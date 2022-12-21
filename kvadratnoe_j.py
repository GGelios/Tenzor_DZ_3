# Написать скрипт решения квадратного уравнения c обработкой отрицательного дискриминанта (с комплексными числами), со случаем, если коэффициенты являются комплексными числами.

import math
import cmath
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
    print('x= ', x)
else:
    x_1=complex((-b+cmath.sqrt(D))/2*a)
    x_2=complex((-b-cmath.sqrt(D))/2*a)
    print('x_1 =', x_1, 'x_2 = ', x_2)
