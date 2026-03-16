N_Hour, N_Min = map(int, input().split())
Make = int(input())

N_Hour += (Make / 60)
N_Hour %= 24
N_Min += (Make % 60)

if N_Min > 59:
    N_Hour += 1
    N_Min -= 60
    if N_Hour > 24:
        N_Hour -= 24    
        print("%d %d" %(N_Hour, N_Min))
    else:
        print("%d %d" %(N_Hour, N_Min))
else:
    print("%d %d" %(N_Hour, N_Min))
