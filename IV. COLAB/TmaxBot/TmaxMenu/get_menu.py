import pyautogui as pg
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://talk.tmaxsoft.com/login.do'
driver.get(url)


def png2click(img_path: str) -> bool:
    img_location = pg.locateOnScreen(img_path)
    if img_location is None:
        return False
    click_location = pg.center(img_location)
    pg.moveTo(click_location)
    pg.click()
    return True


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

driver.implicitly_wait(time_to_wait=5)
first_menu = driver.find_element_by_id('listT0')
first_menu.click()

img_src = driver.find_elements_by_xpath()
# driver.close()
