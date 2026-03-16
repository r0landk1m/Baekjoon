L_num = []

for i in range(10):
    L_num.append(int(input()) % 42)
    
L_num = set(L_num)
        
print(len(L_num))
