T_case = int(input())
money = [[0 for _ in range(4)] for _ in range(T_case)]

for a in range(T_case):
    num = int(input())
    
    money[a][0] = num // 25
    num = num % 25
    money[a][1] = num // 10
    num = num % 10
    money[a][2] = num // 5
    num = num % 5
    money[a][3] = num // 1
    num = num % 1
    
for i in range(T_case):
    for j in range(4):
        print(money[i][j], end = " ")
    print("")
