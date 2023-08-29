import math
def nto(n) :
    for i in range( 2, int(math.sqrt(n)) +1) :
        if n % i ==0:
            return False
    return n > 1

def solve( s) :
    if  nto(len(s)) == False :
        return "NO"
    demnto =0
    dem =0
    for i in range( 0, len(s)) :
        if nto(int(s[i])) :
            demnto +=1
        else :
            dem += 1

    if demnto > dem:
        return "YES"
    return "NO"

for _ in range( int(input())) :
    s = input()
    print(solve(s))