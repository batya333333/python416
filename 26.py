class Rect:
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def show_rect(self):
        print(f'Прямоугольник:\nШирина: {self.__width}\nВысота: {self.__height}')


class RectFon(Rect):
    def __init__(self, height, width, background):
        super().__init__(width, height)
        self.fon = background

    def show_rect(self):
        super().show_rect()
        print('Фон', self.fon, '\n')


class RectBorder(Rect):
    def __init__(self, height, width, width_ram: str, color: str, sol: str):
        super().__init__(height, width)
        self.he = height
        self.wi = width
        self.par1 = width_ram
        self.par2 = color
        self.par3 = sol

    def show_rect(self):
        super().show_rect()
        print('Толщина рамки: ', self.par1)
        print('Тип рамки: ', self.par3)
        print('Цвет рамки: ', self.par2)


shape1 = RectFon(400, 200, 'yellow')
shape1.show_rect()

shape2 = RectBorder(100, 200, '1px', 'blue', 'solid')
shape2.show_rect()
