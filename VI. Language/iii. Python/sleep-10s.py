import time


while True:
    print(time.localtime(time.time()).tm_sec)
    time.sleep(10)
