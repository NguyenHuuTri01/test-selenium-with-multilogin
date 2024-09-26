from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from Models.Email import NewEmail
import time
import Logic.Google_Services as Google
import random
from selenium.webdriver.common.action_chains import ActionChains
from Logic.WriteFile import WriteLinkReview
import os
from pynput.keyboard import Key, Controller
import pyautogui

root_dir = os.getcwd()
src = rf"{root_dir}\ListFile"

def Auto_Review_No_Image(driver: webdriver, linkReview, content, email):
    try:
        # open link review
        driver.get(linkReview)
        # wait and click element tab review
        wait = WebDriverWait(driver, 60)
        tab_danh_gia = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@role="tab"][2]')))
        time.sleep(2)
        driver.execute_script("arguments[0].click();", tab_danh_gia)
        # press tab 3 times and enter for click add review
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.5)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.5)
        actions.send_keys(Keys.RETURN).perform()
        # wait iframe add review
        wait = WebDriverWait(driver, 60)
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@src,"google.com/maps")]')))
        time.sleep(0.5)
        # switch iframe add review
        driver.switch_to.frame(iframe)
        # wait and click element 5 star
        wait = WebDriverWait(driver, 60)
        star = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-rating="5" and @class="s2xyy"]')))
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", star)
        # input content
        input_content = driver.find_element(By.XPATH, '//textarea')
        time.sleep(0.5)
        input_content.send_keys(content)

        # send image
        pathImage = rf"{root_dir}\image"
        files = os.listdir(pathImage)
        files = [f for f in files if os.path.isfile(os.path.join(pathImage, f))]
        if len(files) > 0:
            for file in files:
                wait = WebDriverWait(driver, 60)
                input_content = wait.until(
                    EC.presence_of_element_located((By.XPATH, '//textarea')))
                time.sleep(0.5)
                input_content.click()
                actions.send_keys(Keys.TAB).perform()
                actions.send_keys(Keys.RETURN).perform()

                # switch iframe
                wait = WebDriverWait(driver, 60)
                iframe2 = wait.until(
                    EC.presence_of_element_located((By.XPATH, '//iframe[contains(@src,"docs.google.com/picker")]')))
                time.sleep(0.5)
                # switch iframe add review
                driver.switch_to.frame(iframe2)

                wait = WebDriverWait(driver, 60)
                tab_upload = wait.until(
                    EC.presence_of_element_located((By.XPATH, '//button[@role="tab" and @id="1"]')))
                time.sleep(0.5)
                driver.execute_script("arguments[0].click();", tab_upload)
                time.sleep(1)



                pathfile = os.path.join(os.getcwd(),file)
                wait = WebDriverWait(driver, 60)
                btn_add_file = wait.until(
                    EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
                time.sleep(5)
                btn_add_file.send_keys(pathfile)

                time.sleep(100)


                # driver.switch_to.frame(iframe)

        # # click submit review
        # time.sleep(5)
        # btn_submit = driver.find_element(By.XPATH, '//button[@jsname="IJM3w"]')
        # driver.execute_script("arguments[0].click();", btn_submit)
        # time.sleep(3)
        # # switch default
        # driver.switch_to.default_content()
        # # open url manage review
        # driver.get('https://www.google.com/maps/contrib/')
        # # wait and click element tab my review
        # wait = WebDriverWait(driver, 60)
        # tab_bai_danh_gia = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@role="tab"][2]')))
        # time.sleep(0.5)
        # driver.execute_script("arguments[0].click();", tab_bai_danh_gia)
        # # wait and click element share link
        # btn_share = wait.until(EC.presence_of_element_located((By.XPATH, '(//button//span[contains(@class,"dSlJg google-symbols")])[2]')))
        # time.sleep(0.5)
        # driver.execute_script("arguments[0].click();", btn_share)
        # # wait and get link
        # wait = WebDriverWait(driver, 60)
        # element_link = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))
        # time.sleep(0.5)
        # link_complete = element_link.get_attribute('value')
        # time.sleep(0.5)
        # print(link_complete)
        # # write link on file
        # WriteLinkReview(email, link_complete, rf"{src}\linkComplete.txt")
        # print("[INFO] Review Success")
    except Exception as e:
        print("[INFO] Error Review: ",e)

def Sign_Out_Windows(driver: webdriver):
    driver.get('https://myaccount.google.com/device-activity')
    wait = WebDriverWait(driver, 60)
    element_device = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="X7Lyee"]/div[1]//ul[@class="u7hyyf"]/li[2]')))
    time.sleep(0.5)
    try:
        wd_element =  driver.find_element(By.XPATH, '//div[@class="X7Lyee"]/div[1]//ul[@class="u7hyyf"]/li[2]//p')
        isLoop = False
    except:
        element_device.click()
        wait = WebDriverWait(driver, 60)
        btn_sign_out = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class ="etzm7d"]')))
        time.sleep(0.5)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.5)
        actions.send_keys(Keys.RETURN).perform()
        time.sleep(1)
        wait = WebDriverWait(driver, 60)
        btn_sign_out = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@jsname="LgbsSe"]')))
        time.sleep(0.5)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.5)
        actions.send_keys(Keys.RETURN).perform()
        time.sleep(5)
        driver.refresh()
        time.sleep(2)
        driver.get('https://accounts.google.com/Logout')
        time.sleep(5)