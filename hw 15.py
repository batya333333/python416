def decor(fn):
    def wrapper(*args):
        print('арифметическое',end=' ')
        print(sum(*args)/len(*args))
        return fn(*args)
    return wrapper


@decor
def sm(x):
    return print('сумма',sum(x))


inp=input('Введите числа через пробел: ').split()
x1=tuple(inp)
x1=tuple(map(int,x1))
sm(x1)
