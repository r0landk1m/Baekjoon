N = int(input())
num = 2
factor = []

while True:
    if N % num == 0:
        factor.append(num)
        N /= num
    else:
        num += 1
        
    if N < num:
        break

for a in range(len(factor)):
    print(factor[a])
