#우영우인지 찾기

from collections import deque

def palindrome(s) :
    qa = []
    st = []
    qu = deque()
    

    for x in s :
        if x.isalpha():
            # qa.append(x.lower())
            qu.append(x.lower())
            st.append(x.lower())

    while qu:
        if qu.popleft() != st.pop():
            return False

    
    return True


s = 'Wow'
print(palindrome(s))
