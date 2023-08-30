test = int(input())
star = "*"

for n in range(test):
    blank = " " * (test - 1 - n)
    print("%s%s" %(blank, star))
    star += "*"
