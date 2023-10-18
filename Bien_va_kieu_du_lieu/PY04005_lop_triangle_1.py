from math import sqrt

result = []
class Lop:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return (
            sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
        )


for _ in range(int(input())):
    arr = [int(i) for i in input().split()]
    a = Lop(arr[0], arr[1])
    b = Lop(arr[2], arr[3])
    c = Lop(arr[4], arr[5])
    tmp1 = float(a.distance(b))
    tmp2 = float(a.distance(c))
    tmp3 = float(b.distance(c))
    if (tmp1 + tmp2 <= tmp3) or (tmp1 + tmp3) <= tmp2 or (tmp2 + tmp3) <= tmp1:
        result.append("INVALID")
    else:
        result.append("{:.3f}".format(tmp1 + tmp2 + tmp3))
for i in result  :
    print(i)
