# a=1
# b=2
# a1=a
# a=b
# b=a1
# print(a,b)

class Hello:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def prnt(self):
        print(self.a+self.b)
a=Hello(10,20)
a.prnt()

