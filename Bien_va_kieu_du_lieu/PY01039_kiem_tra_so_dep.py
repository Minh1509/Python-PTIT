def solve(n) :
    for i in range(2, len(n)):
        if n[i] != n[i-2] :
            return "NO"
    return "YES"

t = int(input())
for i in range(t) :
    n = input()
    print(solve(n))