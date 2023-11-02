contry = int(input())
c_range = list(map(int, input().split()))
c_money = list(map(int, input().split()))
A_money = 0

for a in range(contry - 1):
    save = c_range[a]
    c_range[a] = 0
    for b in range(a + 1, contry - 1):
        if c_money[a] < c_money[b]:
            save += c_range[b]
            c_range[b] = 0
        else:
            break
    A_money += save * c_money[a]

print(A_money)