import sys

sys.setrecursionlimit(1000)
a = [-2, 3, 8, -11, -4, 6]


def otric(item_list):
    counter = 0
    if  len(item_list)==0:
        return 0
    if item_list[0]<0:
        counter+=1
    return counter+otric(item_list[1:])


print(otric(a))
