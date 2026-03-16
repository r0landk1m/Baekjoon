k, q, l, b, n, p = map(int, input().split())
right = []

if k != 1:
    right.append(1 - k)
else:
    right.append(0)

if q != 1:
    right.append(1 - q)
else:
    right.append(0)
    
if l != 2:
    right.append(2 - l)
else:
    right.append(0)

if b != 2:
    right.append(2 - b)
else:
    right.append(0)

if n != 2:
    right.append(2 - n)
else:
    right.append(0)
    
if p != 8:
    right.append(8 - p)
else:
    right.append(0)
    
for i in range(6):
    print(right[i], end = " ")
