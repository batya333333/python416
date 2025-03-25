n=str(input('Введите строку: '))
a=n[:n.find('h')]
b=n[n.find('h'):n.rfind('h')+1]
c=n[n.rfind('h')+1:]
print(a+ b[::-1] +c)
