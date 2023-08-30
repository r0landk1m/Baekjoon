Hour, Min = map(int, input().split())

Min -= 45

if Min < 0:
    Hour -= 1
    Min = 60 + Min
    if Hour < 0:
        Hour = 24 + Hour        
        print("%d %d" %(Hour,Min))
    else:
        print("%d %d" %(Hour,Min))
else:
    print("%d %d" %(Hour,Min))
