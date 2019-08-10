i = 0
x = 3
for i in range(100):
    y = i % 10
    if(y == 3):
        print("*")
        x = x + 3
    if (y == 6):
        print("*")
        x = x + 3
    if (y == 9):
        print("*")
        x = x + 3
    else:
        print(i)