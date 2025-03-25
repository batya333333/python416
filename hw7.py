from math import*
choise=int(input('выбор фигуры: '))
if choise==1:
    a=int(input('Введите сторону a: '))
    b=int(input('Введите сторону b: '))
    c=int(input('Введите сторону c: '))
    p=(a+b+c)/2
    s=sqrt((p-a)*(p-b)*(p-c))
    print(s)

if choise==2:
    a2=int(input('Введите сторону a: '))
    b2=int(input('Введите сторону b: '))
    print(a2*b2)

if choise==3:
    r=int(input('Введите радиус r: '))
    print(round(pi*r**2,2))