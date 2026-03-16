M = int(input())
N = int(input())
factor = []
All_sum = 0

for a in range(M, N + 1):
    count = 0
    for b in range(1, a + 1):
        if a % b == 0:
            count += 1
            
        if count > 2:
            break
        
    if count == 2:
        factor.append(a)
        All_sum += a

if All_sum == 0:
    print("-1")
else:
    print(All_sum)
    print(factor[0])
