def solve(s):
    demhoa =0
    demthuong =0
    for x in s:
        if x.islower():
            demthuong += 1
        else :
            demhoa += 1
    if demhoa > demthuong:
        return s.upper()
    else:
        return s.lower()
s = input()
print(solve(s))