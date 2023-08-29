import math
def nto( n) :
    for i in range( 2, int(math.sqrt(n)) +1) :
        if n % i ==0:
            return False
    return n > 1

def solve(s) :
    tmp = ""
    for i in range(len(s) - 4 ,len(s), 1) :
        tmp += s[i]
    if nto(int(tmp)):
        return "YES"
    return "NO"

for _ in range(int(input())) :
    n = input()
    print(solve(n))