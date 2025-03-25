import math
area={
    'Circle': lambda r:math.pi*r**2,
    'Rectangle': lambda a,b: a*b,
    'trap': lambda a,b,h: ((a+b)*h)/2,
}
print(area['Circle'](2))
print(area['Rectangle'](10,13))
print(area['trap'](7,5,3))