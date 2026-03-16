N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = 0

A.sort()
for a in range(N):
    total += A[a] * max(B)
    B.remove(max(B))

print(total)