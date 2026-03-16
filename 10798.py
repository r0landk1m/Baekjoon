All_word = [0] * 5

for i in range(5):
    save = list(input())
    All_word[i] = save
    

for a in range(15):
    for b in range(5):
        try:
            print(All_word[b][a], end = "")
        except:
            print("", end = "")
