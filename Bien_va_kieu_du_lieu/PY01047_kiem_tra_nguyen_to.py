import math
def nto(n) :
    for i in range( 2, int(math.sqrt(n)) +1):
        if n % i ==0:
            return False
    return n > 1
for _ in range(int(input())) :
    s = input()
    res = ""
    for i in range(len(s) -4, len(s)) :
        res += s[i]
    n = int(res)
    if nto(n) == True:
        print("YES")
    else :
        print("NO")
