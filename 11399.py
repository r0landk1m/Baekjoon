N = int(input())
P = list(map(int, input().split()))
P.sort()
A_time = 0

for a in range(N):
    time = 0
    for b in range(a + 1):
        time += P[b]
    A_time += time

print(A_time)