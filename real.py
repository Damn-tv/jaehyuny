i = 0
x = 3
z = 0
for i in range(100):
    y = i % 10
    z = int(i / 10)
    if (y == 9 or y == 6 or y == 3):
        if (z == 9 or z == 6 or z == 3):
            print("**")
    if (z == 9 or z == 6 or z == 3 or y == 9 or y == 6 or y == 3):
        print("*")
    else:
        print(i)