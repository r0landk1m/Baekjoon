S = input()
List = []
english = 97

for x in range(26):
    List.append(-1)

for y in range(26):
    for z in range(len(S)):
        if S[z] == chr(english):
            List[y] = z
            break
    english += 1
            
for p in range(26):
    print(List[p], end = " ")
