import time
import schedule
import Line
from platform import platform


def check_day():
    print(time.strftime('%c', time.localtime(time.time())))


def main():
    print('{:*^60}'.format(' Checking Line & KakaoTalk and take screenshots '))
    schedule.every().day.at('00:01').do(check_day)
    if 'Windows-10' in platform():
        print('This computer is the "InyongLaptop".')
        schedule.every().day.at('06:37').do(Line.job)
    else:
        print('This computer is the "MyNotebook".')
        schedule.every().day.at('18:37').do(Line.job)
    while True:
        print(' Doing Job! ')
        schedule.run_pending()
        time.sleep(30)


if __name__ == '__main__':
    main()
