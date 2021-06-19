import psutil
import os
import subprocess
import time
from tqdm import tqdm
from dataclasses import dataclass
import pyautogui as pg
import win32con
import win32gui
import win32process
from typing import Tuple
from platform import platform

import Key


@dataclass
class Data:
    line: dict
    kakaotalk: dict
    paint: dict
    line_pw: str = ''
    kakaotalk_pw: str = ''
    line_path: str = 'C:\\Users\\Inyong\\AppData\\Local\\LINE\\bin\\LineLauncher.exe'
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
    capture_path: str = 'C:\\Users\\Inyong\\Capture'

    def set_password(self):
        self.line_pw, self.kakaotalk_pw = Key.read()

    def set_line_path(self) -> str:
        return self.line_path.replace('Inyong', 'Administrator')

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


@dataclass
class PointsInyongLaptop:
    line_chatroom: Tuple[int, int] = (1100, 650)
    kakaotalk_chatmenu: Tuple[int, int] = (30, 510)
    kakaotalk_chatroom: Tuple[int, int] = (100, 500)
    system_hide_icon: Tuple[int, int] = (1650, 1060)
    system_right: Tuple[int, int] = (1700, 950)
    system_left: Tuple[int, int] = (1600, 950)


@dataclass
class PointsMyNotebook:
    line_chatroom: Tuple[int, int] = (1050, 520)
    line_disk: Tuple[int, int] = (1150, 600)
    kakaotalk_chatmenu: Tuple[int, int] = (30, 320)
    kakaotalk_chatroom: Tuple[int, int] = (100, 310)
    system_hide_icon: Tuple[int, int] = (1380, 880)
    system_right: Tuple[int, int] = (1420, 765)
    system_left: Tuple[int, int] = (1340, 765)


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
    print('{:*^50}'.format(' wait for on 10 seconds '))
    return time.sleep(10)


def set_paint_on_the_top(app: dict) -> None:
    """
    :param app: paint class name. :return: None.
    """
    app_hwnd = win32gui.FindWindow(app['name'], None)
    win32gui.SetForegroundWindow(app_hwnd)
    return time.sleep(0.5)


def set_line_on_the_top(app: dict) -> any:
    """
    :param app: line text (window name). :return: None.
    """
    app_hwnd = win32gui.FindWindow(None, app['name'])
    win32gui.SetForegroundWindow(app_hwnd)
    return time.sleep(0.5)


def get_hwnd_by_pid(pid) -> None:
    hwnd = win32gui.FindWindow(None, None)
    while hwnd is not None:
        if win32gui.GetParent(hwnd) is not None:
            _, temp_pid = win32process.GetWindowThreadProcessId(hwnd)
            if temp_pid == pid:
                return hwnd
            hwnd = win32gui.GetWindow(hwnd, win32con.GW_HWNDNEXT)
    return None


def set_kakaotalk_on_the_top() -> None:
    for proc in psutil.process_iter():
        if proc.name() == 'KakaoTalk.exe':
            app_hwnd = get_hwnd_by_pid(proc.pid)
            if app_hwnd is not None:
                win32gui.SetForegroundWindow(app_hwnd)
    return time.sleep(0.5)


def login(app) -> None:
    pg.write(app['pw'])
    pg.hotkey('enter')
    return time.sleep(0.5)


def check_line_messages(points) -> None:
    pg.click(points.line_chatroom) # pg.click(x=1100, y=650)
    pg.press('down', presses=6, interval=0.5)
    pg.press('up', presses=6, interval=0.5)
    return time.sleep(0.5)


def check_kakaotalk_chatroom() -> None:
    pg.hotkey('down', 'enter')
    time.sleep(1)
    pg.hotkey('esc')
    return time.sleep(0.5)


def check_kakaotalk_message(points) -> None:
    pg.click(points.kakaotalk_chatmenu) # pg.click(x=30, y=510)
    pg.click(points.kakaotalk_chatroom) # pg.doubleClick(x=100, y=500)
    pg.hotkey('esc')
    for _ in range(40):
        check_kakaotalk_chatroom()
    pg.press('up', presses=50, interval=0.5)
    return time.sleep(0.5)


def take_a_screen_shot(data, cnt: int) -> None:
    pg.press('printscreen')
    turn_process_on_by_win_key(data.paint)
    # set_paint_on_the_top(data.paint)
    pg.hotkey('ctrl', 'v')
    pg.hotkey('ctrl', 's')
    prefix: str = str(time.strftime('%Y-%m-%d-%a', time.localtime(time.time())))
    if cnt == 1:
        postfix: str = '_1 Line'
    elif cnt == 2:
        postfix: str = '_2 KakaoTalk'
    elif cnt == 3:
        postfix: str = '_3 Python'
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


def turn_off_all(data) -> None:
    if turn_process_off(data.paint):
        print('Paint is off.')
        time.sleep(0.5)
    if turn_process_off(data.kakaotalk):
        print('Kakao Talk is off.')
        time.sleep(0.5)
    if turn_process_off(data.line):
        print('Line is off.')
        time.sleep(0.5)


def clean(points) -> None:
    pg.click(points.system_hide_icon)
    time.sleep(0.5)
    pg.moveTo(points.system_right)
    time.sleep(0.5)
    pg.moveTo(points.system_left)
    time.sleep(0.5)
    pg.click(points.system_hide_icon)
    time.sleep(0.5)
    return None


def job():
    data = Data
    data.set_password(data)
    system = platform()
    if 'Windows-10' in system:
        points = PointsInyongLaptop
    else:
        data.line_path = data.set_line_path(data)
        points = PointsMyNotebook
    data.line = data.set_line_dict(data)
    data.kakaotalk = data.set_kakaotalk_dict(data)
    data.paint = data.set_paint_dict(data)
    count: int = 1
    turn_off_all(data)
    print('{:-^50}'.format(' Line '))
    turn_process_on_by_win_key(data.line)
    if 'Windows-10' in system:
        set_line_on_the_top(data.line)
    else:
        pg.click(points.line_disk)
    login(data.line)
    print('{:-^50}'.format(' KakaoTalk '))
    turn_process_on_by_win_key(data.kakaotalk)
    time.sleep(20)
    login(data.kakaotalk)
    print('{:-^50}'.format(' Paint - Print Screen #1 '))
    take_a_screen_shot(data, count)
    count += 1
    if 'Windows-10' in system:
        set_line_on_the_top(data.line)
    check_line_messages(points)
    check_kakaotalk_message(points)
    print('{:-^50}'.format(' Paint - Print Screen #2 '))
    take_a_screen_shot(data, count)
    count += 1
    turn_off_all(data)
    print('{:-^50}'.format(' Paint - Print Screen #3 '))
    take_a_screen_shot(data, count)
    clean(points)
