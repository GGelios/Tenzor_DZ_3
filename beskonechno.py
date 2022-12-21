"""Написать скрипт для движения персонажа влево, вправо, вверх и вниз по координатам x и y по координатной оси, начальная позиция персонажа (0;0), но скрипт бесконечный (каждый раз спрашивается куда движение и выводится результат). Обязательно стоп-слово."""

x=0
y=0
a=0
while True:
    a=input('''Where you go?
    If you print "up" - you going up
    If you print "down" - you going down
    If you print "right" - you going right
    If you print "left" - you going left
    If you print "exit" - script will stoped
    ''' )
    if a=='exit':
        break
    b=int(input('''How many steps?
    '''))
    if a=='up':
        y+=b
    elif a=='down':
        y-=b
    elif a=='right':
        x+=b
    elif a=='left':
        x-=b
    else:
        print('Error')
print ('Your coordinate: x = ', x, 'y = ', y)
