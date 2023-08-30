def odd(a):
    return (2 * a - 1)

N = int(input())

for x in range(N):
    print(" " * (N - x - 1), "*" * odd(x + 1), sep="")
    
for y in range(N - 1):
    print(" " * (y + 1), "*" * odd(N - y - 1), sep="")
