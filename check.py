#富邦防疫保險自動查詢
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time

import requests

import emails
import analyze

def script(account,password,email_address):
    times=0;


    options = Options()
    options.add_argument("--headless")

    browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    browser.get('https://b2c.518fb.com/FubonEC/claims_search.jsp')
      

    time.sleep(2)#等待


    enter=browser.find_element("xpath",'//*[@id="Login-defP0wd-alert"]/div[2]/a')
    enter.click()


    account_input = browser.find_element("id", 'IDNumber')
    password_input = browser.find_element("id", 'IDPWNumber')
    captcha = browser.find_element("id", 'inputRandomNum')
    login = browser.find_element("xpath", '/html/body/section/div/div[2]/div/div/div[2]/form/div[4]/a[2]')

     
    account_input.send_keys(account)  #輸入帳號
    password_input.send_keys(password)  #輸入密碼
    captcha.send_keys(analyze.captcha(browser))  #輸入剛剛擷取的一般驗證碼辨識結果
    login.click()  #點擊登入按鈕
    time.sleep(1)#等待

    while browser.find_element("xpath", '//*[@id="hidden-ch-sm-alert-Error"]/div[1]/p').text=='驗證碼錯誤':
        print(times)
        if times<3:
            times+=1
            browser.find_element("xpath", '//*[@id="hidden-ch-sm-alert-Error"]/div[2]/a').click()

            password_input.send_keys(passowrd)  #輸入密碼
            captcha.send_keys(analyze.captcha(browser))
            login.click()  #點擊登入按鈕
            time.sleep(1)
        if times==3:
            emails.send('富邦保險 自動腳本 發生錯誤已回報系統 造成您的不便 請見諒！',email_address)
            os.system('taskkill /F /IM chrome.exe')

    time.sleep(1)#等待
    if browser.find_element("xpath", '//*[@id="hidden-ID-Error"]/div[1]/p').text=='身分證字號/居留證號輸入錯誤':
        browser.find_element("xpath", '//*[@id="hidden-ID-Error"]/div[2]/a').click()
        emails.send('富邦保險 自動腳本 身分證字號/居留證號輸入錯誤哦！ 請重新設定',email_address)
        os.system('taskkill /F /IM chrome.exe')
    print('ok')

    time.sleep(1)#等待
    unsend = browser.find_element("xpath", '//*[@id="claimsSearch"]/div/div/ul/li[1]/a')
    unsend.click()
    time.sleep(1)#等待
    unsendNum=browser.find_element("id",'unsendNum').text

    progress=browser.find_element("xpath", '//*[@id="claimsSearch"]/div/div/ul/li[2]/a')
    progress.click()
    time.sleep(1)#等待
    progressNum=browser.find_element("id",'progressNum').text

    close=browser.find_element("xpath", '//*[@id="claimsSearch"]/div/div/ul/li[3]/a')
    close.click()
    time.sleep(1)#等待
    closeNum=browser.find_element("id",'closeNum').text

    email_content=unsendNum+"件未送出"
    email_content+=progressNum+"件處理中"
    email_content+=closeNum+"件已結案"
    emails.send(email_content,email_address)

