#안정적인 문자열
"""
}{
{}{}{}
{{{}
---

1. 2
2. 0
3. 1
"""
import sys

result = []
arr = []
while(True) :
    txt = str(sys.stdin.readline().strip())
    if (txt[0] == '-') :
        break

    arr.append(txt)


for j in range(len(arr)):
    count = 0
    st = []

    for i in range(len(arr[j])):
        key = arr[j][i] 
        
        if key == '{' :
            st.append(key)
        elif key == '}' :
            if st :
                st.pop()
            else :
                count += 1
                st.append('}')

    count += len(st)//2
    result.append(count)
        

for idx, val in enumerate(result, start=1):
    print(str(idx)+". "+str(val))

    
