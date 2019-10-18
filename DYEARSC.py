from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import requests
import sys
ops = Options()
ops.add_argument("--headless")
ops.add_argument('--no-sandbox')
ops.add_argument('--disable-dev-shm-usage')
ops.add_experimental_option('excludeSwitches',['enable-automation']) #防止检测window.navigator.webdriver
ops.add_argument('--proxy-server=http://127.0.0.1:9991')
driver = webdriver.Chrome(chrome_options=ops)

resList = []
with open(sys.argv[1],"r") as f:
    for i in f.readlines():
        try:
            res = requests.get(i.strip(" ").strip("\n")).text
            
        except:
            continue
        print(i.strip())
        if res in resList or "QQ空间" in res:
            continue
        else:
            try:
                driver.get(i.strip(" ").strip("\n"))
                resList.append(res)
            except Exception as e:
                print(e)
                continue

        input =  driver.find_elements_by_xpath("//input")

        for elemt in input:
            try:
                elemt.send_keys("admin")
            except:
                pass

        action = driver.find_elements_by_xpath("//*[@type='submit']")
        for q in action:
            try:
                q.click()
            except:
                pass

        action = driver.find_elements_by_xpath("//*[contains(@class,'search')]")
        for q in action:
            try:
                q.click()
            except:
                pass

