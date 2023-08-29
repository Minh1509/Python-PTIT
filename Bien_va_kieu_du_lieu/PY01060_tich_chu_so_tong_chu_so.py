def solve(s) :
    sum =0
    tich =1
    ok = False
    for i in range( 0, len(s)) :
        if i % 2 ==0 :
            if s[i] != '0':
                ok = True
                tich *= int(s[i])
        else :
            sum += int(s[i])
    if ok == True:
        print(tich, end = " ")
        print(sum)
    else :
        print(0, end = " ")
        print(sum)

for _ in range( int(input())) :
    s = input()
    solve(s)
    