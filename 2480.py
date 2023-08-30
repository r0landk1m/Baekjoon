fir, sec, thr = map(int, input().split())

if fir == sec and sec == thr:
    money = 10000 + fir * 1000
    print("%d" %money)
else:
    if fir == sec or sec == thr:
        money = 1000 + sec * 100
        print("%d" %money)
    else:
        if thr == fir:
            money = 1000 + fir * 100
            print("%d" %money)
        else:
            if fir > sec and fir > thr:
                money = fir * 100
                print("%d" %money)
            else:
                if sec > fir and sec > thr:
                    money = sec * 100
                    print("%d" %money)
                else:
                    money = thr * 100
                    print("%d" %money)
