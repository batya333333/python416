# kolvo=int(input('Введите количество студентов: '))
# k=0
# while k<kolvo:
#     print(k+1,'й студент',sep="")
#     name=str(input('Введите имя: '))
#     sr=int(input('Введите средний бал: '))
#     k+=1
# def average(n):
#     srb=

d=dict()
s=0
n=int(input('Введите количество студентов: '))
for i in range(n):
    name=input(str(i+1)+'-й студент: ')
    bal=int(input('Балл: '))
    d[name]=bal
    s+=bal
av=s/n
print(d)
print(av,'студенты с баллом выше среднего:')
for i in d:
    if d[i]>av:
        print(i)