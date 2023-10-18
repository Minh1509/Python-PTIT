class Rectangle :

    def __init__(self, chieudai , chieurong, mausac) :
        self.chieudai = chieudai
        self.chieurong = chieurong
        self.mausac = mausac
    def color(self) :
        return self.mausac[0:1:].upper() + self.mausac[1::].lower()

    def perimeter(self) :
        return (self.chieudai+ self.chieurong) * 2
    def area(self) :
        return self.chieudai * self.chieurong
    
    
if __name__ == '__main__':
    arr = input().split() 
    if int(arr[0]) > 0 and int(arr[1]) > 0:
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
        print("{} {} {}".format(r.perimeter(), r.area(), r.color())) 
    else: print("INVALID")
    