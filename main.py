from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

game_on = True
chrome_drive_path = r"C:\Users\Zach\Desktop\chromedriver_win32\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_drive_path, log_path="NUL"))

driver.get("http://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

def get_cookie_total():
    money = driver.find_element(By.ID, "money").text
    if "," in money:
        money = money.replace(",", "")
        money = int(money)
    return money


def click_cookie():
    cookie_to_click = driver.find_element(By.ID, "cookie")
    cookie_to_click.click()


def buy_upgrade(cookies):
    click_upgrade = int(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text.split(" ")[2].replace(",", ""))
    grandma_upgrade = int(driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text.split(" ")[2].replace(",", ""))
    factory_upgrade = int(driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text.split(" ")[2].replace(",", ""))
    mine_upgrade = int(driver.find_element(By.CSS_SELECTOR, "#buyMine b").text.split(" ")[2].replace(",", ""))
    #print(f"total cookies {cookies}\n click upgrade price: {click_upgrade}\ngrandma upgrade price: {grandma_upgrade}\nfactory upgrade price: {factory_upgrade}\nmine upgrade price: {mine_upgrade}")

    if int(cookies) >= mine_upgrade:
        upgrade = driver.find_element(By.ID, "buyMine")
        upgrade.click()
        print(f"bought mine_upgrade")
    elif int(cookies) >= factory_upgrade:
        upgrade = driver.find_element(By.ID, "buyFactory")
        upgrade.click()
        print(f"Bought factory_upgrade")
    elif int(cookies) >= grandma_upgrade:
        upgrade = driver.find_element(By.ID, "buyGrandma")
        upgrade.click()
        print(f"Bought grandma_upgrade")
    elif int(cookies) >= click_upgrade:
        upgrade = driver.find_element(By.ID, "buyCursor")
        upgrade.click()
        print(f"Bought click_upgrade")
    return


while game_on:
    click_cookie()
    if time.time() > timeout:
        buy_upgrade(get_cookie_total())

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
driver.quit()
