num = int(input())
All_area = 100 * num
base = [[0 for _ in range(100)] for _ in range(100)]

for a in range(num):
    width, hight = map(int, input().split())
    
    for h in range(10):
        for w in range(10):
            base[h + hight - 1][w + width - 1] += 1
            
for i in range(100):
    for j in range(100):
        if base[i][j] > 1:
            All_area -= (base[i][j] - 1)
            
print(All_area)
