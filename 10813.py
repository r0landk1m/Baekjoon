Basket, Play = map(int, input().split())
L_num = []

for x in range(Basket):
    L_num.append(x + 1)

for y in range(Play):
    i, j = map(int, input().split())
    i_num = L_num[i - 1]
    L_num[i - 1] = L_num[j - 1]
    L_num[j - 1] = i_num
        
for z in range(Basket):
    print(L_num[z], end=" ")
