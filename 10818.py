N = int(input())
List_num = list(map(int, input().split()))
MAX = List_num[0]
MIN = List_num[0]

for n in range(N):
    if List_num[n] > MAX:
        MAX = List_num[n]
    
    if List_num[n] < MIN:
        MIN = List_num[n]
        
print(MIN, MAX)
