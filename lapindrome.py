T = int(input())
for i in range(T):
    n = input()
    l = len(n)
    if l % 2 == 0:
        b, c = n[:l//2], n[l//2:]
    else:
        b, c = n[:l//2], n[l//2+1:]
    if sorted(b) == sorted(c):
        print("YES")
    else:
        print("NO")
