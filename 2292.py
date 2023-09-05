N = int(input())
room = 1
block = 1

while N > block:
    block += room * 6
    room += 1
    
print(room)
