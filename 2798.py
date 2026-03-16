N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = 0

for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            S = num[a] + num[b] + num[c]
            if S <= M and result < S:
                result = S

print(result)