charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(int(input())):
    s = ""
    N, b = map(int, input().split())
    while N > 0:
        s += charset[N % b]
        N //= b
    print(s[::-1])
