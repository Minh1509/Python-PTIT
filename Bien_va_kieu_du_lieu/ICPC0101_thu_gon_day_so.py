n = int(input())
a = [int(i) for i in input().split()]

st = []
for i in a :
    
    if len(st) > 0 :
        tmp = st.pop()
        if ( i + tmp) % 2 !=0:
            st.append(tmp)
            st.append(i)
        else :
            continue
                
    else : 
        st.append(i)
print(len(st))