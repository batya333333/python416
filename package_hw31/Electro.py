from package_hw31 import Auto


class Electro(Auto.Auto):
    def __init__(self, pow):
        self.pow = pow

    def pr_info(self):
        print(f'Этот автомобиль имеет мощность {self.pow}')
