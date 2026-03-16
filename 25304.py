T_money = int(input())
T_num = int(input())
My_money = 0

for i in range(T_num):
    money, count = map(int, input().split())
    My_money += money * count
    
if T_money == My_money:
    print("Yes")
else:
    print("No")
