import random
c = 0
b = 0
a = []
for i in range(10):
    a.append(random.randrange(-100,100))
print(a)
for i in range(10):
    if(b < 0):
        b = 0 + a[i]
    else:
        b = b + a[i]
    if(b> c):
        c = b
    print(a)
print(c)