N = int(input())
dot = 2
A_dot = 0

for a in range(N):
    dot = dot * 2 - 1
    A_dot = dot * dot
    
print(A_dot)
