def makelist():
    a = []
    b = 0
    for i in range(8):
        a.append(int(input()))
    return a
def findmaxlist(a):
    max = []
    for j in range(5):
        temp = 0
        for i in range(len(a)):
            if(a[temp] < a[i]):
                temp = i
        max.append(a[temp])
        a[temp] = -1
    return max
def caltotal(max):
    total = 0
    for i in range(len(max)):
        total += max[i]
        return total
def printmax(max,total):
    print(total)
    for i in range(len(max)):
        print(max)