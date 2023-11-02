A, B = map(int, input().split())

for a in range(min(A, B)):
    if max(A, B) * (a + 1) % min(A, B) == 0:
        print(max(A, B) * (a + 1))
        break