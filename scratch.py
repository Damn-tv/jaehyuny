import random
a = []
m = 0
x = 0

for i in range(10):
    flag = 0
    if (i == 0):
        a.append(random.randrange(-100, -1))
    else:
        b = random.randrange(-100, -1)
        for i in range(len(a)):
            if(a[i] == b):
                flag = 1
                break
        if(flag == 0):
            a.append(b)



s = a[0]


print(a)
#for i in range():
for x in range(10):
    if(s < a[x]):
        s = a[x]
print(s)