import math


class Square():

    counter=0
    @staticmethod
    def rectangle1(a, b, c):
        p = math.ceil((a + b + c) // 2)
        p2 = math.ceil(math.sqrt(p*((p - a) * (p - b) * (p - c))))
        Square.counter+=1
        return p2

    @staticmethod
    def rectangle2(a,b):
        s=(a*b)/2
        Square.counter += 1
        return s

    @staticmethod
    def kvadrat(a):
        s=a**2
        Square.counter += 1
        return s

    @staticmethod
    def pryamoyg(a,b):
        s=a*b
        Square.counter += 1
        return s

print('Площадь треугольника по формуле Герона: ',Square.rectangle1(3,4,5))
print('Площадь треугольника по высоте и стороне: ',Square.rectangle2(6,7))
print('Площадь квадрата: ',Square.kvadrat(7))
print('Площадь прямоугольника: ',Square.pryamoyg(2,6))
print('Количество подсчетов площади: ', Square.counter)