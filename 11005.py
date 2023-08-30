N, B = map(int, input().split())

arithmetic = []

while True:
    if N < B:
        if N % B > 9:
            arithmetic.append(chr(N % B + 55))
        else:
            arithmetic.append(N % B)
        break
    
    if N % B == 0:
        arithmetic.append(0)
    else:
        if N % B > 9:
            arithmetic.append(chr(N % B + 55))
        else:
            arithmetic.append(N % B)
        
    N = N // B
    

print(*arithmetic[::-1], sep = "")
