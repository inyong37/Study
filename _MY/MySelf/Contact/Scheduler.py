from time import sleep
import schedule
from platform import platform
from subprocess import call

import Line

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import Print


def commit():
    call('cd ../BootCamp/ && python -c "from Contribution import job; job(True)"', shell=True)


def main():
    print('{:*^60}'.format(' Checking Line & KakaoTalk and take screenshots '))
    schedule.every().day.at('00:10').do(Print.day)
    interval: int = 30
    cnt: int = 0
    system = platform()
    if 'Windows-10' in system:
        print('{: ^60}'.format('This computer is "InyongLaptop".'))
        schedule.every().day.at('06:37').do(Line.job)
        # sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
        # from BootCamp import Contribution
        # schedule.every().day.at('10:34').do(Contribution.job, False)
        schedule.every().day.at('01:00').do(commit)
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
