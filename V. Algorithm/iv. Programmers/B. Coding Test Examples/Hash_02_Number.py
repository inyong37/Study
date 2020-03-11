# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-11-Wed
# Programmers
# Coding Test Examples/Hash_02_Number
# 코딩테스트 연습/해시/전화번호 목록

# Try 1

def solution(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book)-1):
        index_number = phone_book[i]
        check_number = phone_book[i+1]
        if list(set(index_number).intersection(check_number)):
            return False
    return True

# Try 2

def solution(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book)):
        index_number = phone_book[i]
        for j in range(1, len(phone_book)):
            check_number = phone_book[j]
            if i is j:
                pass
            else:
                if index_number in check_number:
                    print(index_number, check_number)
                    return False
    return True

# Try 3

def solution(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book)):
        index_number = phone_book[i]
        for j in range(1, len(phone_book)):
            check_number = phone_book[j]
            if i is j:
                pass
            else:
                if index_number in check_number:
                    print(index_number, check_number)
                    return False
    for i in range(len(phone_book)-1, 0, -1):
        index_number = phone_book[i]
        for j in range(len(phone_book)-1, 1, -1):
            check_number = phone_book[j]
            if i is j:
                pass
            else:
                if index_number in check_number:
                    print(index_number, check_number)
                    return False
    return True

# Try 4: string.startswith()

def solution(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book)-1):
        check_number = phone_book[i]
        if phone_book[i+1].startswith(check_number):
            return False
    return True
