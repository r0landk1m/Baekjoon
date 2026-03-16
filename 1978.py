N = int(input())
num = list(map(int, input().split()))
All_count = 0
    
for a in num:
    count = 0
    for b in range(a):
        if a % (b + 1) == 0:
            count += 1
            
    if count == 2:
        All_count += 1
        
print(All_count)
