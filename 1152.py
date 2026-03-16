N = input()
word = 0
N = N.strip()

if len(N) != 0:
    word = 1

for x in range(len(N)):
    if N[x] == " ":
        word += 1
        
print(word)
