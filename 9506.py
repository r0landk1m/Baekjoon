N = int(input())
while N != -1:
    factor = [0]
    for a in range(N):
        if N % (a + 1) == 0 and N != (a + 1):
            factor.append(a + 1)
            factor[0] += (a + 1)
            
    if factor[0] == N:
        print(N, "=", end = " ")
        for b in range(len(factor) - 1):
            print(factor[b + 1], end = " ")
            if b != len(factor) - 2:
                print("+", end = " ")
        print("")
    else:
        print(N, "is NOT perfect.")
    
    N = int(input())
