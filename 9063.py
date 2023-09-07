coordi = []
N = int(input())

for i in range(N):
    save = list(map(int, input().split()))
    coordi.extend(save)
    
MIN_x = coordi[0]
MIN_y = coordi[1]
MAX_x = coordi[0]
MAX_y = coordi[1]
    
for x in range(2, N * 2, 2):
    if coordi[x] < MIN_x:
        MIN_x = coordi[x]

for y in range(3, N * 2, 2):
    if coordi[y] < MIN_y:
        MIN_y = coordi[y]

for mx in range(2, N * 2, 2):
    if coordi[mx] > MAX_x:
        MAX_x = coordi[mx]

for my in range(3, N * 2, 2):
    if coordi[my] > MAX_y:
        MAX_y = coordi[my]

print((MAX_x - MIN_x) * (MAX_y - MIN_y))
