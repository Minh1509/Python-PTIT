t = int(input())
for i in range(t) :
    n, x, m = map(float, input().split())
    
    dem =0
    while n < m:
        tmp = ( n * x )/ 100
        n += tmp
        dem += 1

    print(dem)