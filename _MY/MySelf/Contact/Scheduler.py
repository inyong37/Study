from time import sleep
import schedule
from platform import platform

import Line

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import Print


def main():
    print('{:*^60}'.format(' Checking Line & KakaoTalk and take screenshots '))
    schedule.every().day.at('00:10').do(Print.day)
    interval: int = 30
    cnt: int = 0
    system = platform()
    if 'Windows-10' in system:
        print('{: ^60}'.format('This computer is "InyongLaptop".'))
        schedule.every().day.at('06:37').do(Line.job)
    elif 'Windows-7' in system:
        print('{: ^60}'.format('This computer is "MyNotebook".'))
        schedule.every().day.at('18:37').do(Line.job)
    else:
        print('{: ^60}'.format('This computer is "UNKNOWN".'))
        print(' Nothing to do. ')
        exit()
    while True:
        Print.work(count=cnt)
        cnt += 1
        if cnt == 4:
            cnt = 0
        schedule.run_pending()
        sleep(interval)


if __name__ == '__main__':
    main()
