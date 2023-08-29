def solve(s) :
    sum =0
    tich =1
    ok = False
    for i in range(0, len(s)):
        if i % 2 ==0 :
            sum += int(s[i])
        else :
            if int(s[i]) != 0 :
                ok = True
                tich *= int(s[i])
    if ok == True :
        print(sum , end = " ")
        print(tich)
    else :
        print(sum , end = " ")
        print(0)

for _ in range(int(input())):
    s = input()
    solve(s)