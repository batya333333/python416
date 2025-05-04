class Auto:
    def __init__(self, brand, model, ye, usage):
        self.brand = brand
        self.model = model
        self.ye = ye
        self.usage = usage

    def info(self):
        print(self.brand, self.model, self.ye, self.usage)