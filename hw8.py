from random import randint
a=[]
for i in range(10):
    a.append(randint(1,100))
print(a)
mIn=min(a)
print('min: ',mIn)
# if mIn in a:
#     ind=a.index(mIn)
#     print(ind)
ind=a.index(mIn)
print('index_min: ',ind)
dels=a[ind:]
print(dels)