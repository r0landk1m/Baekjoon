Basket, Play = map(int, input().split())
L_num = []

for x in range(Basket):
    L_num.append(0)

for y in range(Play):
    F, E, num = map(int, input().split())
    run = E - F + 1
    
    for i in range(run):
        L_num[F - 1] = num
        F += 1
        
for z in range(Basket):
    print(L_num[z], end=" ")
