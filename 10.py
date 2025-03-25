from random import*
def dobavlenie(kon):
    first=tuple([randint(0,5) for i in range(10)])
    second=tuple([randint(-5,0) for i in range(10)])
    kon=first+second
    c=kon.count(0)
    return c,kon
print(dobavlenie(1))

