#
# NEOBANK（住信SBIネット銀行）サイトへログイン
#

import time
import json
import webbrowser
from pathlib import Path

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

login_info = json.load(open("login_info.json", "r", encoding="utf-8"))

site_name = "bank_neo"

url_login = login_info[site_name]["url"]

USER = login_info[site_name]["id"]
PASS = login_info[site_name]["pass"]

dldir_path = Path('./').resolve()

print(dldir_path)

# Firefoxのヘッドレスモードを有効にする
options = ChromeOptions()
# options.add_argument('--headless')
options.add_experimental_option("prefs", {
    "download.default_directory": str(dldir_path),
    "plugins.always_open_pdf_externally": True
})


# chromeprofile =

# Firefoxを起動する
browser = Chrome(options=options)

# ログイン画面取得
browser.get(url_login)


# 入力
e = browser.find_element(By.ID, "userNameNewLogin")
# e = browser.find_element(By.CLASS_NAME, "m-formWrap ng-star-inserted")
print(e)

e.clear()
e.send_keys(USER)
# e = browser.find_element(By.CSS_SELECTOR, "loginPwdSet")
e = browser.find_element(By.ID, "loginPwdSet")
e.clear()
e.send_keys(PASS)

# ログイン
button = browser.find_element(By.CSS_SELECTOR, ".m-btnEm-l > span")
button.click()

# ページロード完了まで待機
WebDriverWait(browser, 15).until(
    ec.presence_of_element_located((By.CLASS_NAME, "top-name"))
)

# 画面描画が完全に終わるまで、念の為スリープ入れる
# time.sleep(3)

# ログインできたか確認（画面キャプチャ取る）
browser.save_screenshot("home.png")

balance = browser.find_element(By.CSS_SELECTOR, "body > app > div:nth-child(3) > ng-component > div > main > ng-component > div.m-hdr-bankAc > div > nb-titlecarousel > div > div > ul > li > div > div > strong").text


print(balance, "円の残高.")

# time.sleep(3)
browser.find_element(By.XPATH, "/html/body/app/div[1]/ng-component/div/main/ng-component/div[3]/nb-gethtml-dynamic[1]/ul/li[3]/a").click()

browser.save_screenshot("meisai.png")

browser.find_element(By.XPATH, "/html/body/app/div[1]/ng-component/div/main/ng-component/section/div/nb-gethtml-dynamic[1]/div/ul/li[2]/a").click()

browser.save_screenshot("debitcard.png")
time.sleep(3)
# browser.find_element(By.XPATH, "/html/body/app/div[1]/ng-component/div/main/ng-component/section/div/div/div[2]/ul/li[1]/a").screenshot("csvbutton.png")
csvdlbutton = browser.find_element(By.XPATH, "/html/body/app/div[1]/ng-component/div/main/ng-component/section/div/div/div[2]/ul/li[1]/a")
csvdlbutton.click()
# time.sleep(3)
# href = csvdlbutton.get_attribute("href")
# print(href)
browser.quit()

print("=== All done! ===")