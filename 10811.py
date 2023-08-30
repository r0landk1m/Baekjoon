n, m = map(int, input().split())
basket = []

for x in range(n):
    basket.append(x + 1)
    
for y in range(m):
    i, j = map(int, input().split())
    num = 0
    
    save = []
    for s in range(i - 1, j):
        save.append(basket[s])
    save.reverse()
    
    for z in range(i - 1, j):
        basket[z] = save[num]
        num += 1
    
for p in range(n):
    print(basket[p], end = " ")
