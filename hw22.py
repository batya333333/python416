class Auto:

    def __init__(self,name,year,manufacture,engine_pover,color,price):
        print('Данные автомобиля '.center(40,"*"),"\n")
        self.name=name
        self.year=year
        self.manufacture=manufacture
        self.engine_pover=engine_pover
        self.color=color
        self.price=price

    def print_info(self):
        print(f'Название модели: {self.name}\nГод выпуска: {self.year}\n'
              f'Производитель: {self.manufacture}\nМощьность двиагателя: {self.engine_pover}\n'
              f'Цвет машины: {self.color}\nЦена: {self.price}',"\n")
        print('='*40)

    def set_name(self,name):
        self.name=name

    def get_name(self):
        print(self.name)
        print(f'Название модели: {self.name}\nГод выпуска: {self.year}\n'
              f'Производитель: {self.manufacture}\nМощьность двиагателя: {self.engine_pover}\n'
              f'Цвет машины: {self.color}\nЦена: {self.price}', "\n")

    def set_manufactere(self,manufacture):
        self.manufacture=manufacture

    def get_manufacture(self):
        print(self.manufacture)
        print(f'Название модели: {self.name}\nГод выпуска: {self.year}\n'
              f'Производитель: {self.manufacture}\nМощьность двиагателя: {self.engine_pover}\n'
              f'Цвет машины: {self.color}\nЦена: {self.price}', "\n")

    def set_year(self,year):
        self.year=year

    def get_year(self):
        print(self.year)
        print(f'Название модели: {self.name}\nГод выпуска: {self.year}\n'
              f'Производитель: {self.manufacture}\nМощьность двиагателя: {self.engine_pover}\n'
              f'Цвет машины: {self.color}\nЦена: {self.price}', "\n")

    def set_engine(self, engine_pover):
        self.engine_pover = engine_pover

    def get_eng(self):
        print(self.engine_pover)
        print(f'Название модели: {self.name}\nГод выпуска: {self.year}\n'
              f'Производитель: {self.manufacture}\nМощьность двиагателя: {self.engine_pover}\n'
              f'Цвет машины: {self.color}\nЦена: {self.price}', "\n")

    def set_color(self, color):
        self.color = color

    def get_color(self):
        print(self.color)
        print(f'Название модели: {self.name}\nГод выпуска: {self.year}\n'
              f'Производитель: {self.manufacture}\nМощьность двиагателя: {self.engine_pover}\n'
              f'Цвет машины: {self.color}\nЦена: {self.price}', "\n")

    def set_price(self, price):
        self.price = price

    def get_price(self):
        print(self.price)
        print(f'Название модели: {self.name}\nГод выпуска: {self.year}\n'
              f'Производитель: {self.manufacture}\nМощьность двиагателя: {self.engine_pover}\n'
              f'Цвет машины: {self.color}\nЦена: {self.price}', "\n")


# X7 M50i 2021 BMW 530 white 1079000

p1=Auto('X7 M50i',2021, 'BMW', 530, 'white', 1079000)
p1.print_info()

p1.set_engine(400)
p1.get_eng()