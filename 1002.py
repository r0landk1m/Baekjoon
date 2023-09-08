T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        two_range = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)

        if two_range > r1 + r2 or two_range < abs(r1 - r2):
            print(0)
        elif two_range == r1 + r2 or two_range == abs(r1 - r2):
            print(1)
        else:
            print(2)
