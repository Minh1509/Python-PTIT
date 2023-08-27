def solve(n) :
    dem4 = n.count('4')
    dem7 = n.count('7')
    if dem4 +dem7 < len(n) :
        return False
    return True
t = int(input())
for i in range (t) :
    n = input()
    if solve(n) == True:
        print("YES")
    else:
        print("NO")
