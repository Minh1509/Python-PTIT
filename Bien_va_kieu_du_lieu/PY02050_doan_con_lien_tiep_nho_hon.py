for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    print(1, end = " ")
    for i in range(1, len(a), 1) :
        dem =1
        tmp = i-1
        while tmp >= 0:
            if a[tmp] <= a[i] :
                dem += 1
                tmp -= 1
            else :
                break
        print(dem , end= " ")
    print()

