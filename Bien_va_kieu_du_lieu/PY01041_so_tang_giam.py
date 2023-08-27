def solve(n) :
    if n < 100 :
        return "NO"
    ok = False
    s= str(n)
    j =0
    for i in range(len(s)-1):
        if s[i+1] == s[i]:
            return "NO"
        elif s[i+1] < s[i] :
            j =i 
            ok = True
            break
    if ok == False:
        return "NO"
    else :
        for i in range(j, len(s)-1 ):
            if s[i+1] >= s[i] :
                return "NO"
    return "YES"

t = int(input())
for _ in range(t) :
    n = int(input())
    print(solve(n))