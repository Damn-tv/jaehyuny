v = int(input())
t = 0
i = 1
for i in range(2, int(v/2)+1):
    if(v % i == 0):
        t = 1
if(t == 1):
    print("not prime")
else:
    print("prime")
