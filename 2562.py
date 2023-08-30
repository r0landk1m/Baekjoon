N = 9
L_num = []
MAX = 0
line = 0

for i in range(N):
    L_num.append(int(input()))

for n in range(N):
    if L_num[n] > MAX:
        MAX = L_num[n]
        line = n + 1

print("%d\n%d" %(MAX, line))
