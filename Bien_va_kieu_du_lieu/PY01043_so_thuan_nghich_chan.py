def solve(n):
    if n != int(str(n)[::-1]) or len(str(n)) % 2 == 1:
        return False
    dem = 0
    while n > 0:
        a = n % 10
        if a % 2 != 0:
            return False
        n //= 10

    return True


for _ in range(int(input())):
    n = int(input())
    for i in range(22, n,2):
        if solve(i):
            print(i, end=" ")
    print()
