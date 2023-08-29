for _ in range(int(input())) :
    n = input()
    tich =1
    for i in n :
        if int(i) != 0:
            tich *= int(i)
    print(tich)