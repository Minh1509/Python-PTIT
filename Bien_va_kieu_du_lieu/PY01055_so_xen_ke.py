import math
def solve(s) :
    if len(s) % 2 ==0 or s[0] == s[1] :
        return False
    for i in range(0, len(s)-2, 2) :
        if s[i] != s[i+2] :
            return False
    return True

for _ in range(int(input())) :
    n = input()
    if solve(n):
        print("YES")
    else :
        print("NO")