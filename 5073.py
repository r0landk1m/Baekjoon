while True:
    a, b, c = map(int, input().split())
    if a == b and b == c and a == 0:
        break
    
    if max(a, b, c) < (a + b + c - max(a, b, c)):
        if a == b and b == c:
            print("Equilateral")
        elif a == b or b == c or c == a:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")
