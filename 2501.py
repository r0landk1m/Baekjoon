N, K = map(int, input().split())
count = 0

for a in range(N):
    if N % (a + 1) == 0:
        count += 1
    
    if count == K:
        print(a + 1)
        break

if count < K:
    print("0")
