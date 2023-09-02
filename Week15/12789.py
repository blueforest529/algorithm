"""
도키도키 간식드리미

5
5 4 1 3 2
"""

import sys

N = int(input())
list = list(map(int,input().split()))
st = []
cnt = 1


while list:
    if cnt == list[0] :
        cnt+=1
        list.pop(0)
    else:
        st.append(list.pop(0)) # 기달림
        
    while st :
        if st[-1] == cnt:
            st.pop()
            cnt+=1
        else :
             break
    

# while list:
#     print(list[0])
#     print(cnt)
#     if cnt==list[0]:
#         cnt+=1
#         list.pop(0)
#     else:
#         st.append(list.pop(0))

#     while st:
#         if st[-1] == cnt:
#             st.pop()
#             cnt+=1
#         else:
#             break
        
print(st)