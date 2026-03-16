L_num = []

for x in range(1, 31):
    L_num.append(x)

for y in range(28):
    L_num.remove(int(input()))
    
for z in range(2):
    print(L_num[z])
