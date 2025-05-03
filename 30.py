import math
from abc import ABC, abstractmethod
from math import *


class Shape:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_perimetr(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def get_perimetr(self):
        return self.side * 4

    def get_area(self):
        return self.side * self.side

    def draw(self):
        return ('* ' * self.side + "\n") * self.side

    def info(self):
        print(
            f'=== Квадрат ===\nСторона: {self.side}\nЦвет: {self.color}\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimetr()}\n'
            f'{self.draw()}')


class Rectangle(Shape):
    def __init__(self, lenght, width, color):
        super().__init__(color)
        self.lenght = lenght
        self.width = width

    def get_perimetr(self):
        return (self.lenght + self.width) * 2

    def get_area(self):
        return self.lenght * self.width

    def draw(self):
        return ('* ' * self.width + "\n") * self.lenght

    def info(self):
        print(
            f'=== Прямоугольник ===\nДлина: {self.lenght}\nШирина: {self.width}\nЦвет: {self.color}\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimetr()}\n'
            f'{self.draw()}')


class Triaangle(Shape):
    def __init__(self, side_1, side_2, side_3, color):
        super().__init__(color)
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def get_perimetr(self):
        return self.side_1 + self.side_3 + self.side_2

    def get_area(self):
        p = self.get_perimetr() / 2
        return round(sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)), 2)

    def draw(self):
        arr = []
        for i in range(self.side_2):
            arr.append(" " * i + '*' * (self.side_1 - 2 * i))
        return "\n".join(reversed(arr))

    def info(self):
        print(
            f'=== Треугольник ===\nСторона1: {self.side_1}\nСторона2: {self.side_2}\nСторона3: {self.side_3}\nЦвет: {self.color}\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimetr()}\n'
            f'{self.draw()}')


sq = Square(3, 'red')
sq.info()

rect = Rectangle(3, 7, 'green')
rect.info()

treug = Triaangle(11, 6, 6, 'yell')
treug.info()
