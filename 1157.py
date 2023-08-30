S = input()
Alpha = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
in_Alpha = []
count = 0

for x in range(26):
    in_Alpha.append(0)
    
for y in range(len(S)):
    for z in range(26):
        if S[y] in Alpha[z]:
            in_Alpha[z] += 1

for n in range(26):
    if max(in_Alpha) == in_Alpha[n]:
        count += 1

if count > 1:
    print("?")
else:
    print(Alpha[in_Alpha.index(max(in_Alpha))][0])
