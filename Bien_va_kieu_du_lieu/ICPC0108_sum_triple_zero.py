for _ in range(int(input())):
    n = int(input())
    arr = sorted([int(i) for i in input().split()])

    res = 0
    for i in range(0, n-2) :
        left = i +1
        right = n-1

        while( left < right) :
            tmp = arr[i] + arr[left] + arr[right]
            if not tmp :
                res += 1
                left += 1
            if tmp < 0:
                left += 1
            else :
                right -=1
    print(res)