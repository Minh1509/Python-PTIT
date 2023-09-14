for _ in range( int(input())) :
    n = int(input())
    m = {}
    cnt = 0
    a = [int(i) for i in input().split()]
    for i in a :
        if i in m :
            m[i] += 1
        else :
            m[i] = 1
        cnt =  max(cnt, m[i])
    ok = False
    for i in m :
        if m[i] == cnt and m[i] > n /2 :
            ok = True
            print(i)
            break
    if ok == False:
        print("NO")   
    