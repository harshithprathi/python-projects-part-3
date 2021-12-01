r=int(input())
for i in range(r, 0, -1):
    for j in range(i, 0, -1):
        if i == 1 or i == r or j == 1 or j == i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
