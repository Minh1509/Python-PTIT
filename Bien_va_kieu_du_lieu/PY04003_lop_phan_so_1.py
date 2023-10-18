from math import gcd
class PhanSo :
    def __init__(self, tu, mau) :
        self.tu = int(tu)
        self.mau = int(mau)

    def rutgon(self) :
        g =  gcd(self.tu , self.mau)
        self.tu = int(self.tu / g)
        self.mau = int(self.mau / g)
        
        
    def output(self) :
        print(self.tu, "/", self.mau, sep = "")


if __name__== '__main__' :
    tu, mau = [int(x) for x in input().split()]
    ps = PhanSo(int(tu), int(mau))
    ps.rutgon()
    ps.output()

    
        