a, b, c, d, e, f = map(int, input().split())

if (a * e) == (b * d):
  if a == b == 0 or d == e == 0:
    print(0, 0)
  elif b == e == 0:
    if a != 0:
      x = c / a
    else:
      x = f / d
    print("%d 0" %(x))
  else:
    if b != 0:
      y = c / b
    else:
      y = f / e
    print("0 %d" %(y))
else:
  y = (c * d - a * f) / (b * d - a * e)
  if a != 0:
    x = (c - b * y) / a
  else:
    x = (f - e * y) / d

print("%d %d" %(x, y))