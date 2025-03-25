a=int(input('Введите число от 1 до 99: '))
a1=a
if 11<=a1<=14:
    print(a,'копеек')
elif 1<=a<=10 or 15<=a<=99:
    a1=a1%10
    if a1==1:
        print(a,'копейка')
    elif 2<=a1<=4:
        print(a,'копейки')
    else:
        print(a,'копеек')
else:
    print('Неправильный диапозон')