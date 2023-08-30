N, Find_num = map(int, input().split())
List_num = list(map(int, input().split()))
wrong = 0

for i in range(N):
    if List_num[i - wrong] >= Find_num:
        del List_num[i - wrong]
        N -= 1
        wrong += 1
        
for i in range(N):
    print(List_num[i])
