from time import sleep, strftime, localtime, time

from Language import korean


def day():
    print(strftime('%c', localtime(time())))


def start(work_name='Test'):
    korean()
    print(f' Starting: {work_name:>20}')


def work(version=1, count=0):
    if count is 0:
        postfix = '|'
        count += 1
    elif count is 1:
        postfix = '/'
        count += 1
    elif count is 2:
        postfix = '-'
        count += 1
    else:
        postfix = '\\'
        count = 0

    if version is 0:
        content = '  Doing Job' + '.' * (count + 1)
    else:
        content = '  Doing Job ' + postfix
    print(content, end='\r')


def work_legacy(interval=1, version=1):
    korean()
    cnt = 0
    while True:
        if cnt is 0:
            postfix = '|'
            cnt += 1
        elif cnt is 1:
            postfix = '/'
            cnt += 1
        elif cnt is 2:
            postfix = '-' # 'ㅡ'
            cnt += 1
        else:
            postfix = '\\'
            cnt = 0

        if version is 0:
            content = '  Doing Job' + '.' * (cnt+1)
        else:
            content = '  Doing Job ' + postfix
        print(content, end='\r')
        sleep(interval)
