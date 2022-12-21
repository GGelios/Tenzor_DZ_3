"""Написать скрипт для движения персонажа влево, вправо, вверх и вниз по координатам x и y по координатной оси, начальная позиция персонажа (0;0)"""

x=0
y=0
a=input('''Where you go axis y?
If you print "up" - you going up
If you print "down" - you going down
''' )
a_1=input('''Where you go axis x?
If you print "right" - you going right
If you print "left" - you going left
''')
b=int(input('''How many steps axis y?
'''))
b_1=int(input('''How many steps axis x? 
'''))
if a=='up':
   y+=b
elif a=='down':
    y-=b
else:
    print('Error')
if a_1=='right':
    x+=b_1
elif a_1=='left':
    x-=b_1
else:
    print('Error')
print ('Your coordinate: x = ', x, 'y = ', y)
