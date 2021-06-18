from os import system
from platform import platform


def korean():
    system('chcp 65001') if 'Windows' in platform() else system('LANG=ko_KR; export LANG')