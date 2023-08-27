def check(s) :
    n = len(s)
    for i in range(1, n) :
        if abs(ord(s[i] )- ord(s[i-1])) != abs(ord(s[n-i]) - ord(s[n-i-1])):
            return "NO"
    return "YES"
t = int(input())
for i in range(t) :
    s = input().strip()
    result = check(s)
    print(result)