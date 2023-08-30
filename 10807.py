N = int(input())
T_num = 0
L_num = list(map(int, input().split()))
Find_num = int(input())

for i in range(N):
    if L_num[i] == Find_num:
        T_num += 1
        
print(T_num)
