from time import sleep, strftime, localtime, time

from Language import korean


def day():
    print(strftime('%c', localtime(time())))


def start(work_name='Test'):
    korean()
    print(f' Starting: {work_name:>20}')


def work(version: int = 1, count: int = 0):
    if count == 0:
        postfix = '|'
        count += 1
    elif count == 1:
        postfix = '/'
        count += 1
    elif count == 2:
        postfix = '-'
        count += 1
    else:
        postfix = '\\'
        count = 0

    if version == 0:
        content = '  Doing Job' + '.' * (count + 1)
    else:
        content = '  Doing Job ' + postfix
    print(content, end='\r')


def work_legacy(interval: int = 1, version: int = 1):
    korean()
    cnt = 0
    while True:
        if cnt == 0:
            postfix = '|'
            cnt += 1
        elif cnt == 1:
            postfix = '/'
            cnt += 1
        elif cnt == 2:
            postfix = '-' # 'ㅡ'
            cnt += 1
        else:
            postfix = '\\'
            cnt = 0

        if version == 0:
            content = '  Doing Job' + '.' * (cnt+1)
        else:
            content = '  Doing Job ' + postfix
        print(content, end='\r')
        sleep(interval)
