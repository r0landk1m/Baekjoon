Sec_list = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9):
    save = list(map(int, input().split()))
    for j in range(9):
        Sec_list[i][j] = save[j]
        
MAX = max(map(max, Sec_list))

print(MAX)

for a in range(9):
    for b in range(9):
        if Sec_list[a][b] == MAX:
            print(a + 1, b + 1)
            break
