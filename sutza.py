a = (int(input()))
b = (int(input()))
c = 0
def p(a,b):
    c = a + b
    return c

def m(a,b):
    c = a - b
    return c

def x(a,b):
    c = a * b
    return c

def n(a,b):
    c = a / b
    return c

d = (input())
if(d == p):
    c = p(a,b)
elif(d == m):
    c = m(a,b)
elif(d == x):
    c = x(a,b)
elif(d == n):
    c = n(a,b)
print(c)