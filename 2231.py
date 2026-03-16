N = int(input())

for a in range(N):
    num = str(a)
    S = a
    for b in range(len(num)):
        S += int(num[b])
    if S == N:
        print(a)
        break
    if a == N - 1:
        print(0)