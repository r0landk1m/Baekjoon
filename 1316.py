Ward_num = int(input())
Count = 0

for a in range(Ward_num):
    Alpha = [[0 for i in range(26)] for j in range(2)] 
    Alpha_use = []
    ward = input()

    for b in range(26):
        Alpha[0][b] = 97 + b

    for c in ward:
        Alpha[1][ord(c) - 97] += 1
    
    C = 0
    for d in range(26):
        if Alpha[1][d] > 1:
            Alpha_use.append([])
            Alpha_use[C].append(Alpha[0][d])
            Alpha_use[C].append(Alpha[1][d])
            C += 1

    count_num = 0
    for e in range(len(Alpha_use)):
        F_a = chr(Alpha_use[e][0])
        F = ward.find(F_a)
        
        for f in range(Alpha_use[e][1]):
            if ward[F + f] == F_a:
                count_num += 1
    
    Alpha_num = 0
    for q in range(len(Alpha_use)):
        Alpha_num += Alpha_use[q][1]
    
    if count_num == Alpha_num:
        Count += 1

print(Count)
