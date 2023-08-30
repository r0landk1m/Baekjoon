S = input()
Croa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
Croa_count = [0] * 8
Count = len(S)

for x in range(len(Croa_count)):
    if Croa[x] in S:
        Croa_count[x] += S.count(Croa[x])

if (Croa_count[7] - Croa_count[2]) >= 0:
    Croa_count[7] -= Croa_count[2]
    
Count -= sum(Croa_count)
Count -= Croa_count[2]

print(Count)
