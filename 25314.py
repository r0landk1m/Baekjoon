L = ""
T_num = int(input())

if (T_num % 4) == 0:
    num = T_num // 4
else:
    num = T_num // 4 + 1

for i in range(num):
    L += "long "
    if i == (num - 1):
        print("%sint" %L)
