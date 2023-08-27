def check(s) :
    return s == '0' or s == '1' or s == '2'

for i in range(int(input())):
    s = input()
    ok = True
    for i in s:
        if check(i) == False:
            ok = False
            print("NO")
            break
    if ok == True :
        print("YES")

