from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

start_time = time.time() + 5
end_time = time.time() + 300
game_on = True

cookie = driver.find_element(by=By.CSS_SELECTOR, value=("#cookieAnchor #bigCookie"))

def cookie_counter():
    driver.implicitly_wait(1)
    cookies = driver.find_element(by=By.CSS_SELECTOR, value=("#cookies.title")).text.split('\n')
    return cookies[1]


def purchase():
    try:
        list_of_products = driver.find_elements(by=By.CSS_SELECTOR, value=("#store #products .enabled"))
        list_of_products[-1].click()
    except:
        pass
    try:
        upgrade = driver.find_element(by=By.XPATH, value=("/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div[1]")).click()
    except:
        pass
    try:
        bonus_cookie = driver.find_element(by=By.CSS_SELECTOR, value=(".shimmer")).click()
    except:
        pass
while game_on:
    current_time = time.time()
    cookie.click()
    if current_time > start_time:
        purchase()
    if current_time >= end_time:
        print(cookie_counter())
        game_on = False

driver.quit()
