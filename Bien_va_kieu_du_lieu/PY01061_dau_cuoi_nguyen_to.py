import math
def nto( n) :
    for i in range( 2, int(math.sqrt(n)) +1):
        if n % i ==0 :
            return False
    return n > 1
def solve(s ):
    sodau = ""
    socuoi = ""
    for i in range( 0, 3) :
        sodau += s[i]
    for i in range( len(s) -3, len(s)):
        socuoi += s[i]
    if nto(int(sodau)) and nto(int(socuoi)):
        print("YES")
    else :
        print("NO")


for _ in range( int(input())) :
    s = input()
    solve(s)
