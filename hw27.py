class Student:
    def __init__(self):
        self.name1 = 'Roman'
        self.name2 = 'Vladimir'
        self.desk = self.Desktop()

    def print_info(self):
        print(self.name1, *self.desk.print_info())
        print(self.name2, *self.desk.print_info())

    class Desktop:
        def __init__(self):
            self.desk = 'HP'
            self.model = 'I7'
            self.mem = 16

        def print_info(self):
            return '=>', self.desk, self.model, self.mem


info = Student()
info.print_info()
