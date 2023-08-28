def solve(n) :
    if n <= 10 or n != int(str(n)[::-1]):
        return False
    return True

for _ in range(int(input())) :
    n = input()
    sum =0
    for i in n :
        sum += int(i)
    if solve(sum) :
        print("YES")
    else:
        print("NO")