stage = []

for _ in range(10):
	stage.append(list(map(int, input().split())))

y = 1
out = 0
if stage[y][1] == 0:
	for i in range(1, 9):
		stage[y][i] = 9

		if stage[y][i+1] == 1:
			while stage[y][i+1] != 0 and y < 9:
				y += 1
				if stage[y][i] == 0:
					stage[y][i] = 9
				elif stage[y][i] == 2:
					stage[y][i] = 9
					out = 1
					break
			if out == 1:
				break
		elif stage[y][i+1] == 2:
			stage[y][i+1] = 9
			break
		else:
			continue
else:
	print("Error")


for i in range(10):
	for j in range(10):
		print(stage[i][j], end=' ')
	print()