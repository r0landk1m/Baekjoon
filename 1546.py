subject = int(input())
exam = list(map(int, input().split()))
average = 0.0

MAX = max(exam)
    
for y in range(subject):
    exam[y] = exam[y] / MAX * 100
    average += exam[y]

average /= subject

print(average)
