def seting ():
    a = input()
    flag = 0
    b = []
    temp = ['c','a','m','b','r','i','d','g','e']
    return (flag,b,temp,a)

def check (a , temp,b,flag):
    for l in range(len(a)):
        for i in range(len(temp)):
            if(a[l] == temp[i]):
                flag = 1
        if (flag == 0):
            b.append(a[l])
            flag = 0

def print (b):
    b = ''.join(b)
    print(b)

seting()
check(a, temp, b, flag)
print(b)
