import psutil
import os
import subprocess
from tqdm import tqdm
from dataclasses import dataclass
import pyautogui as pg
import win32gui
import time
from typing import Tuple


@dataclass
class Data:
    line_pw: str
    kakaotalk_pw: str
    line: dict
    kakaotalk: dict
    paint: dict
    line_path: str = 'C:\\Users\\Administrator\\AppData\\Local\\LINE\\bin\\LineLauncher.exe'
    kakaotalk_path: str = 'C:\\Program Files (x86)\\Kakao\\KakaoTalk\\KakaoTalk.exe'
    paint_path: str = 'C:\\Windows\\System32\\mspaint.exe'
    line_key: str = '2'
    kakaotalk_key: str = '3'
    paint_key: str = '7'
    line_exe: str = 'LINE.exe'
    kakaotalk_exe: str = 'KakaoTalk.exe'
    paint_exe: str = 'mspaint.exe'
    line_name: str = 'LINE'
    kakaotalk_name: str = ''
    paint_name: str = 'MSPaintApp'
    capture_path: str = 'C:\\Users\\Administrator\\Desktop\\Capture'

    def set_line_dict(self) -> dict:
        line = {
            'pw': self.line_pw,
            'path': self.line_path, 'key': self.line_key,
            'exe': self.line_exe, 'name': self.line_name}
        return line

    def set_kakaotalk_dict(self) -> dict:
        kakaotalk = {
            'pw': self.kakaotalk_pw,
            'path': self.kakaotalk_path, 'key': self.kakaotalk_key,
            'exe': self.kakaotalk_exe, 'name': self.kakaotalk_name}
        return kakaotalk

    def set_paint_dict(self) -> dict:
        paint = {
            'path': self.paint_path, 'key': self.paint_key,
            'exe': self.paint_exe, 'name': self.paint_name}
        return paint


data = Data
data.line = data.set_line_dict(data)
data.kakaotalk = data.set_kakaotalk_dict(data)
data.paint = data.set_paint_dict(data)


def search_exe_path() -> Tuple[str, str, str]:
    """
    Deprecated function, because of cost of searching
    :return:
    paths of line, kakaotalk, and paint.
    """
    for dirpath, dirname, filename in tqdm(os.walk('C:\\')):
        if filename == 'LineLauncher.exe':
            line_path: str = dirpath + filename
        if filename == 'KakaoTalk.exe':
            kakaotalk_path: str = dirpath + filename
        if filename == 'mspaint.exe':
            paint_path: str = dirpath + filename
        return Tuple[line_path, kakaotalk_path, paint_path]


def check_process_alive(app: dict) -> bool:
    """
    Check the app is alive.
    :param:
    App's exe name.
    :return:
    If the process is alive, return True, else return False.
    """
    for proc in psutil.process_iter():
        if app['exe'].lower() == proc.name().lower():
            return True
    return False


def turn_process_on_by_path(app: dict) -> None:
    subprocess.call(app['path'])
    return time.sleep(5)


def turn_process_on_by_win_key(app: dict) -> None:
    pg.hotkey('winleft', app['key'])
    return time.sleep(10)


def set_paint_on_the_top(app: dict) -> None:
    """
    :param app: paint class name. :return: None.
    """
    app_hwnd = win32gui.FindWindow(app['name'], None)
    win32gui.SetForegroundWindow(app_hwnd)
    return time.sleep(0.5)


def set_line_on_the_top(app: dict) -> None:
    """
    :param app: line text (window name). :return: None.
    """
    app_hwnd = win32gui.FindWindow(None, app['name'])
    win32gui.SetForegroundWindow(app_hwnd)
    return time.sleep(0.5)


def login(app) -> None:
    pg.write(app['pw'])
    pg.hotkey('enter')
    return time.sleep(0.5)


def check_line_messages() -> None:
    # pg.click(x=1100, y=650)
    pg.click(x=1050, y=520)
    pg.press('down', presses=6, interval=0.5)
    pg.press('up', presses=6, interval=0.5)
    return time.sleep(0.5)


def check_kakaotalk_chatroom() -> None:
    pg.hotkey('down', 'enter')
    time.sleep(1)
    pg.hotkey('esc')
    return time.sleep(1)


def check_kakaotalk_message() -> None:
    # pg.click(x=30, y=510)
    pg.click(x=30, y=320)
    # pg.doubleClick(x=100, y=500)
    pg.doubleClick(x=100, y=310)
    pg.hotkey('esc')
    for _ in range(20):
        check_kakaotalk_chatroom()
    pg.press('up', presses=25, interval=0.5)
    return time.sleep(0.5)


def take_a_screen_shot(cnt: int) -> None:
    pg.press('printscreen')
    turn_process_on_by_win_key(data.paint)
    set_paint_on_the_top(data.paint)
    pg.hotkey('ctrl', 'v')
    pg.hotkey('ctrl', 's')
    prefix: str = str(time.strftime('%Y-%m-%d-%a', time.localtime(time.time())))
    if cnt == 1:
        postfix: str = '_1 Line'
    elif cnt == 2:
        postfix: str = '_2 KakaoTalk'
    elif cnt == 3:
        postfix: str = '_3 PyCharm'
    else:
        postfix: str = '_4 Test'
    file_name = prefix + postfix
    print(file_name)
    pg.write(file_name)
    time.sleep(1)
    pg.hotkey('enter')
    time.sleep(1)
    turn_process_off(data.paint)
    return time.sleep(5)


def turn_process_off(app: dict) -> bool:
    """
    :param
    name: process exe name to turn off.
    :return:
    If the process is already off return True,
    else turn off and return True; return or check_process_alive().
    """
    if not check_process_alive(app):
        return True
    prefix: str = 'TASKKILL /F /IM '
    postfix: str = ' /T'
    command = prefix + app['exe'] + postfix
    print(command)
    os.system(command)
    return not check_process_alive(app)


def turn_off_all() -> None:
    if turn_process_off(data.paint):
        print('Paint is off.')
        time.sleep(0.5)
    if turn_process_off(data.kakaotalk):
        print('Kakao Talk is off.')
        time.sleep(0.5)
    if turn_process_off(data.line):
        print('Line is off.')
        time.sleep(0.5)


def job():
    # def main():
    count: int = 1
    turn_off_all()
    print('='*10 + 'Line' + '='*10)
    turn_process_on_by_win_key(data.line)
    # set_line_on_the_top(data.line)
    login(data.line)
    print('='*10 + 'KakaoTalk' + '='*10)
    turn_process_on_by_win_key(data.kakaotalk)
    time.sleep(10)
    login(data.kakaotalk)
    print('=' * 10 + 'Paint Before' + '=' * 10)
    take_a_screen_shot(count)
    count += 1
    check_line_messages()
    check_kakaotalk_message()
    print('='*10 + 'Paint After' + '='*10)
    take_a_screen_shot(count)
    count += 1
    turn_off_all()
    print('=' * 10 + 'Paint Ended' + '=' * 10)
    take_a_screen_shot(count)


# if __name__ == '__main__':
#     main()


"""
output of taskkill:
성공: PID 14776인 프로세스(PID 9012인 자식 프로세스)가 종료되었습니다.
성공: PID 10224인 프로세스(PID 9012인 자식 프로세스)가 종료되었습니다.
성공: PID 19148인 프로세스(PID 9012인 자식 프로세스)가 종료되었습니다.
성공: PID 9012인 프로세스(PID 10148인 자식 프로세스)가 종료되었습니다.
성공: PID 11340인 프로세스(PID 10652인 자식 프로세스)가 종료되었습니다.
"""
