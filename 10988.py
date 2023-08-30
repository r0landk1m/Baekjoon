word = input()
re_word = word[::-1]

if str(word) == str(re_word):
    print("1")
else:
    print("0")
