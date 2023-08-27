def solve(s) :
    for i in range(0, len(s)-1, 1):
        if s[i+1] < s[i]:
            return False
    return True 
t = int(input())
for i in range(t):
    n = input()
    if solve(n) :
        print("YES")
    else:
        print("NO")


