x, y, w, h = map(int, input().split())
w = abs(w - x)
l = abs(h - y)

print(min(w, l, x, y))
