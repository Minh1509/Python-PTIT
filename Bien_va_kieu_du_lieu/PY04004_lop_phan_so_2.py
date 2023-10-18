from math import gcd


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutgon(self):
        g = gcd(self.tu, self.mau)
        self.tu = int(self.tu / g)
        self.mau = int(self.mau / g)

    def cong(self, other):
        a = self.tu * other.mau + self.mau * other.tu
        b = self.mau * other.mau
        self.tu = a
        self.mau = b

    def output(self):
        print(self.tu, "/", self.mau, sep="")


arr = [int(i) for i in input().split()]
x = PhanSo(arr[0], arr[1])
y = PhanSo(arr[2], arr[3])
x.cong(y)
x.rutgon()
x.output()
