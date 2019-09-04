# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 13. 회문 찾기


def palindrome(s):
    qu = []
    st = []
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True


print(palindrome('Wow'))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))

from collections import deque

qu = deque()
qu.append(1)
qu.append(2)
print(qu)
qu.popleft()
print(qu)
