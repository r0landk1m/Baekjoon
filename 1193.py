X = int(input())
count = 2
edge = 1
line = 1

for seque in range(X):
    if seque == edge:
        line += 1
        edge += count
        count += 1

a = (X - (edge - count + 1))
b = (line + 1) - a
if line % 2 == 0:
    print("%d/%d" %(a, b))
else:
    print("%d/%d" %(b, a))
