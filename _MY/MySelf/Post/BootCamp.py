from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyautogui as pg
import time

import Key


@dataclass
class Example:
    name: str = ''
    birthday: str = ''
    date: str = ''


@dataclass
class Data:
    name: str = ''
    birthday: str = ''
    date: str = ''
    sex: str = ''
    phone: str = ''
    tool_dir = '../../../IV. COLAB/Bot//tool/'
    url = 'https://www.katc.mil.kr/katc/community/children.jsp'


ex = Example
data = Data
test = True
if test:
    [ex.name, ex.birthday, ex.date], [data.name, data.birthday, data.date, data.phone, data.sex] = Key.read(test)
else:
    [data.name, data.birthday, data.date, data.phone, data.sex] = Key.read(test)

driver = webdriver.Chrome(data.tool_dir + 'chromedriver.exe')
driver.maximize_window()
driver.get(data.url)

# Check Person
select = Select(driver.find_element_by_id("search_val1"))
select.select_by_visible_text(ex.date)
driver.find_element_by_css_selector("#birthDay").send_keys(ex.birthday)
driver.find_element_by_css_selector("#search_val3").send_keys(ex.name)
driver.find_element_by_css_selector("#item_body > div.sub_wrap > div > div > div.lo_765_left > div:nth-child(3) > div > div > div.child_search_wrap > form > fieldset > input.btn_05").click()
driver.find_element_by_css_selector("#childInfo1").click()
driver.implicitly_wait(1)
driver.find_element_by_css_selector("#letterBtn").click()

# Identity Verification
driver.find_element_by_css_selector("#jwxe_main_content > div > div > div.btn_wrap > form > a").click()

# driver.implicitly_wait(3000)
# Web Page 1
time.sleep(3)
pg.click(370, 360)
pg.click(130, 605)
pg.click(315, 605)
pg.click(130, 630)
pg.click(315, 630)
pg.click(300, 680)

# Web Page 2
time.sleep(3)
pg.click(450, 260)
pg.click(350, 430)
pg.write(data.name)
pg.click(260, 480)
pg.write(data.birthday)
pg.click(380, 480)
pg.hotkey('1')
pg.write(data.sex)
pg.click(350, 530)

pg.write(data.phone)

