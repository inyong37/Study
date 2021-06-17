"""
This code is to get menu png or xlsx from web site.
"""

from dataclasses import dataclass
import pyautogui as pg
from selenium import webdriver


@dataclass
class Data:
    id = ''
    pw = ''
    tool_dir = 'tool\\'
    img_dir = 'img\\'
    url = 'https://talk.tmaxsoft.com/login.do'


"""
Function with selenium.
"""


def main():
    data = Data
    """
    Functions with py auto gui. 
    """

    def png2click(img_path: str) -> bool:
        img_location = pg.locateOnScreen(img_path)
        if img_location is None:
            return False
        click_location = pg.center(img_location)
        pg.moveTo(click_location)
        pg.click()
        return True

    def multiple_check(num: int, path: str) -> None:
        for i in range(num):
            print(i)
            if png2click(path):
                break

    def func_by_func():
        multiple_check(10, data.tool_dir + 'talk_id.PNG')
        pg.write(data.id)
        multiple_check(10, data.tool_dir + 'talk_password.PNG')
        pg.write(data.pw)
        multiple_check(10, data.tool_dir + 'talk_login.PNG')
        multiple_check(10, data.tool_dir + 'talk_alarm.PNG')
        multiple_check(10, data.tool_dir + 'talk_menu.PNG')

    def hand_by_hand():
        if not png2click(data.tool_dir + 'talk_id.PNG'):
            png2click(data.tool_dir + 'talk_id.PNG')
        pg.write(data.id)
        if not png2click(data.tool_dir + 'talk_password.PNG'):
            png2click(data.tool_dir + 'talk_password.PNG')
        pg.write(data.pw)
        if not png2click(data.tool_dir + 'talk_login.PNG'):
            png2click(data.tool_dir + 'talk_login.PNG')
        if not png2click(data.tool_dir + 'talk_alarm.PNG'):
            png2click(data.tool_dir + 'talk_alarm.PNG')
        if not png2click(data.tool_dir + 'talk_menu.PNG'):
            png2click(data.tool_dir + 'talk_menu.PNG')

    driver = webdriver.Chrome(data.tool_dir + 'chromedriver.exe')
    driver.maximize_window()
    driver.get(data.url)
    id_element = driver.find_element_by_id('id')
    id_element.send_keys(data.id)
    pw_element = driver.find_element_by_id('pass')
    pw_element.send_keys(data.pw)
    pw_element.submit()
    alarm_elements = driver.find_elements_by_xpath("//*[text()='알리미']")
    print(alarm_elements)
    alarm_elements[1].click()
    menu_elements = driver.find_elements_by_xpath("//*[text()='식단표']")
    menu_elements[1].click()

    # driver.implicitly_wait(time_to_wait=5)

    first_menu = driver.find_element_by_id('listT0')
    first_menu.click()

    image_elements = driver.find_elements_by_tag_name('img')
    image_source = image_elements.get_attribute('src')

    # driver.close()


if __name__ == '__main__':
    main()
