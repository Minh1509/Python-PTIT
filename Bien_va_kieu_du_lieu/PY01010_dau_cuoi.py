def solve(s) :
    tmp1 = s[0] + s[1]
    n = len(s)-1
    tmp2 = s[n-1] + s[n]
    if tmp1 == tmp2:
        return True
    return False
t = int(input())
for i in range(t) :
    n = input()
    if solve(n) == True:
        print("YES")
    else :
        print("NO")