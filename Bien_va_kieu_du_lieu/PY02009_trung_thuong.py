for _ in range( int(input())) :
    n = int(input())
    m , cnt = {}, 0
    for x in range(n) :
        i = int(input())
        if i in m :
            m[i] += 1
        else :
            m[i] = 1
        cnt = max(cnt, m[i])

    ans = 1000
    for i in m :
            if m[i] == cnt :
                ans = min(ans, i) 
    print(ans)
