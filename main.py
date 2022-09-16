import sys
import time
import env
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 隱藏自動化測試標籤
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(executable_path="./chromedriver", options=option)
# driver.execute_script('navigator.webdriver = null;')
remain = 0
TRY = 0
success = False

driver.get("https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/")


# driver.set_window_size(1920, 1080)


def login():
    driver.switch_to.default_content()
    driver.switch_to.frame('bookmark')
    driver.find_element(By.NAME, "id").send_keys(env.STUDENT_ID)
    driver.find_element(By.NAME, "password").send_keys(env.PASS)
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


def remain_1():  # 7500021_02 科學飲茶實務
    driver.find_element(By.ID, "itemTextLink4").click()  # 加選及加簽
    driver.switch_to.default_content()
    driver.switch_to.frame(3)
    driver.find_element(By.CSS_SELECTOR, "td:nth-child(8) input:nth-child(7)").click()
    driver.find_element(By.ID, "cge_cate2").click()
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(8)").click()
    driver.find_element(By.CSS_SELECTOR, "#form1 > input:nth-child(7)").click()
    re = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(10) > th:nth-child(4)").text
    # 7500021_02 科學飲茶實務 上次篩選後餘額
    return int(re)


def select_1():  # 7500021_02 科學飲茶實務
    driver.find_element(By.CSS_SELECTOR, "tr:nth-child(10) input").click()
    driver.find_element(By.CSS_SELECTOR, "table:nth-child(10) > tbody > tr > th > input").click()


# random.seed(time.time(), 2)
while True:
    driver.refresh()
    login()
    for i in range(100):
        try:
            sleepsec = 0.3
            TRY = TRY + 1
            remain = remain_1()
            if remain > 0:
                print("\nremain: " + str(remain))
                print("try " + str(TRY) + " times.")
                select_1()
                success = True
                print("Success")
                break
            else:
                print(f"\rtried {TRY} times", "." * (TRY % 10 + 1), end="", file=sys.stderr)
                # time.sleep(sleepsec)
                driver.switch_to.default_content()
                driver.switch_to.frame('bookmark')
        except NoSuchElementException:
            driver.refresh()
    if success:
        break

input()
driver.quit()
