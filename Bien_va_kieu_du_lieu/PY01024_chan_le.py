import math

def solve(s) :
    sum =0
    for i in range(0, len(s)-1, 1) :
        if abs(int(s[i+1]) - int(s[i])) !=2:
            return False
        sum += int(s[i])
    sum += int(s[len(s)-1])
    if sum % 10 !=0 :
        return False
    return True
t = int(input())
for i in range(t):
    s = input()
    if solve(s) == True:
        print("YES")
    else :print("NO")
