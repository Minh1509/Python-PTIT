def solve(s) :
    s1 = s[::-1]
    for i in range( 1, len(s)) :
        tmp1 =ord(s[i]) - ord(s[i-1])
        tmp2 = ord(s1[i]) -ord( s1[i-1])
        if abs(tmp1) != abs(tmp2) : 
            return "NO"
    return "YES"

for _ in range( int(input()))  :
    s = input()
    print(solve(s))
