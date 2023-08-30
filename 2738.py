N, M = map(int, input().split())
A = [[0 for _ in range(M)] for _ in range(N)] 
Sum = [[0 for _ in range(M)] for _ in range(N)] 

for i in range(N):
    save = list(map(int, input().split()))
    for j in range(M):
        A[i][j] = save[j]

for a in range(N):
    save = list(map(int, input().split()))
    for b in range(M):
        Sum[a][b] = save[b] + A[a][b]

for p in range(N):
    for q in range(M):
        print(Sum[p][q], end = " ")
    print("")
