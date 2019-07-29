a = int(input())
flag = 0

for i in range(2, int(a/2)):
    if(a % i == 0):
        flag = 1
        break

if(flag == 0):
    print("prime")
else:
    print("Not prime")
