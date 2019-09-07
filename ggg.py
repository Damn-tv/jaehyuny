def list (a,b):
    for i in range(1, a):
        if(a % i == 0):
            b.append(i)
    return(a,b)

def check (b,c):
    for j in range(len(b)):
        c = c+b[j]
    return (c,b)

def printi (a,c):
    if(a == c):
       print('완전수')
    else:
        print('안완전수')

a = int(input())
b = []
c = 0
a,b = list(a, b)
c,b = check(b, c)
print(c, b)
printi(a, c)