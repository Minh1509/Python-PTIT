import math

def nto( n) :
    for i in range(2, int(math.sqrt(n)) +1) :
        if n % i ==0:
            return False
    return n > 1

def solve(s) :
    demnto =0
    dem =0
    if nto(len(s)) == False:
        return False
    for i in s:
        if nto(int(i)) :
            demnto +=1
        else :
            dem+=1
    if demnto > dem:
        return True
    return False
for _ in range(int(input())) :
    s = input()
    if solve(s) :
        print("YES")
    else :
        print("NO")

