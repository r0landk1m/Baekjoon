N, K = map(int, input().split())
money = []
money_num = 0

for _ in range(N):
    money.append(int(input()))
money.reverse()

for a in range(N):
    if K // money[a] > 0:
        money_num += K // money[a]
        K -= money[a] * (K // money[a])

print(money_num)