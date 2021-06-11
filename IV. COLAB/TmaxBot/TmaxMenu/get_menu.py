import pyautogui as pg
from selenium import webdriver
import requests

driver = webdriver.Chrome()
url = 'https://talk.tmaxsoft.com/login.do'
driver.maximize_window()
driver.get(url)
id = 'inyong_hwang'
pw = ''

id_element = driver.find_element_by_id('id')
id_element.send_keys(id)
pw_element = driver.find_element_by_id('pass')
pw_element.send_keys(pw)
pw_element.submit()
alarm_elements = driver.find_elements_by_xpath("//*[text()='알리미']")
print(alarm_elements)
alarm_elements[1].click()
menu_elements = driver.find_elements_by_xpath("//*[text()='식단표']")
menu_elements[1].click()


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
    multiple_check(10, 'talk_id.PNG')
    pg.write('inyong_hwang')
    multiple_check(10, 'talk_password.PNG')
    pg.write('')
    multiple_check(10, 'talk_login.PNG')
    multiple_check(10, 'talk_alram.PNG')
    multiple_check(10, 'talk_menu.PNG')


def hand_by_hand():
    if not png2click('talk_id.PNG'):
        png2click('talk_id.PNG')
    pg.write('inyong_hwang')
    if not png2click('talk_password.PNG'):
        png2click('talk_password.PNG')
    pg.write('')
    if not png2click('talk_login.PNG'):
        png2click('talk_login.PNG')
    if not png2click('talk_alram.PNG'):
        png2click('talk_alram.PNG')
    if not png2click('talk_menu.PNG'):
        png2click('talk_menu.PNG')


# driver.implicitly_wait(time_to_wait=5)

first_menu = driver.find_element_by_id('listT0')
first_menu.click()

image_elements = driver.find_elements_by_tag_name('img')
image_source = image_elements.get_attribute('src')

# driver.close()
