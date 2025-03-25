# def outer(a,b,c):
#     def inner(i,j):
#         return i*j
#     s= 2*(inner(a,b)+inner(a,c)+inner(b,c))
#     return s
# print(outer(2,4,6))
# print(outer(5,8,2))
# print(outer(1,6,8))
#
# s=0
# def outer(a,b,c):
#     def inner(i,j):
#         return i*j
#
#     global s
#     s= 2*(inner(a,b)+inner(a,c)+inner(b,c))
#     return s
#
# print(outer(2,4,6))
# print(outer(5,8,2))
# print(outer(1,6,8))
#
# def outer(a,b,c):
#     s=0
#     def inner(i,j):
#         nonlocal s
#         s+=i*j
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#     s= 2*s
#     return s
# print(outer(2,4,6))
# print(outer(5,8,2))
# print(outer(1,6,8))

# l1=[1,2,3]
# l2=[4,5,6]
# print(list(map(lambda a,b: (a+b),l1,l2)))

# lst=[input()for i in range(5)]
# print(lst)
# lst=list(map(int,lst))
# print(lst)

