def solve(s , k):
    encode = ""
    for x in s:
      index = P.index(x)
      tmp = P[(index + k) % 28]
      encode += tmp
    return encode

def reverse1(s) :
   return s[::-1]     
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while(True) :
    str = input()
    k, s = str.split()
    k = int(k)
    if k == 0 :
      break
    encoded = solve(s, k)
    reverse_encode = reverse1(encoded)
    print(reverse_encode)
    
    
    