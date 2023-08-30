Alpha = input()
num = []
total = 0

for x in range(len(Alpha)):
    num.append(ord(Alpha[x]) - 65)
    
for y in range(len(Alpha)):
    if (num[y] // 3) > 4:
        if num[y] >= 15 and num[y] <= 18:
            total += 8
        elif num[y] >= 19 and num[y] <= 21:
            total += 9
        else:
            total += 10
    else:
        total += num[y] // 3 + 3

print(total)
