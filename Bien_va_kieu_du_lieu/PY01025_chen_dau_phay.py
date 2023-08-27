s = input()
s = s[::-1]
cnt =0
tmp = ""
for i in range(0, len(s)):
    
   
    if cnt ==3 :
        cnt =0
        tmp += ","
    cnt += 1
    tmp += s[i]
tmp = tmp[::-1]
print(tmp)