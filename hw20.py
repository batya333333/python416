text='Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл'
#
with open('text.txt','w') as f:
    f.write(text)
#
pos1=int(input('Выбрать позицию: '))
pos2=int(input('Выберите позицию куда заменять: '))

if pos2>pos1 and pos1==1 and pos2==2:
    with open('text.txt' ,'r') as fr:
        r=fr.readlines()
        r[0]='Замена строки в текстовом файле;\n'
        r[1]='записать список в файл;\n'
        r[2]='изменить строку в списке;\n'
        # print(r)
    with open('text.txt','w') as fr2:
        r2=fr2.writelines(r)
    with open('text.txt') as p:
        p1=p.readlines()
        res=list(map(str,p1))
        print(''.join(res))

elif pos1==0 and pos2==1:
    with open('text.txt', 'r') as fr:
        r=fr.readlines()
        r[0]='изменить строку в списке;\n'
        r[1]='Замена строки в текстовом файле;\n'
        r[2]='записать список в файл;\n'
        # print(r)
    with open('text.txt','w') as fr2:
        r2=fr2.writelines(r)
    with open('text.txt') as p:
        p1=p.readlines()
        res=list(map(str,p1))
        print(''.join(res))

else:
    print('Некорректный индекс')


