for _ in range(int(input())) :
    s = input()
    v = []
    tmp = ""
    for char in s :
        if char.isdigit() :
            tmp += char
        else :
            v.append(int(tmp))
            tmp = ""
    print(min(v))