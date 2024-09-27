from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Models.Email import NewEmail
from Models.InfoAccount import NewInfo
import time
from selenium.webdriver.common.action_chains import ActionChains


def GG_Login(driver: webdriver, email: NewEmail) -> bool:
    try:
        driver.get("https://accounts.google.com/")

        wait = WebDriverWait(driver, 60)
        input_email = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        input_email.send_keys(email.email)
        input_email.send_keys(Keys.ENTER)

        wait = WebDriverWait(driver, 60)
        input_password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password'][@name='Passwd']")))
        time.sleep(2)
        input_password.send_keys(email.password)
        input_password.send_keys(Keys.ENTER)

        try:
            wait = WebDriverWait(driver, 10)
            click_recovery = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-challengeid='5']")))
            time.sleep(2)
            click_recovery.click()

            wait = WebDriverWait(driver, 10)
            input_recovery = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
            time.sleep(2)
            input_recovery.send_keys(email.recovery)
            input_recovery.send_keys(Keys.ENTER)
        except:
            try:
                wait = WebDriverWait(driver, 10)
                input_recovery = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
                time.sleep(2)
                input_recovery.send_keys(email.recovery)
                input_recovery.send_keys(Keys.ENTER)
            except:
                print("[INFO] No need to enter Recovery")

        try:
            time.sleep(3)
            actions = ActionChains(driver)
            actions.send_keys(Keys.TAB).perform()
            time.sleep(1)
            actions.send_keys(Keys.TAB).perform()
            time.sleep(1)
            actions.send_keys(Keys.TAB).perform()
            time.sleep(1)
            actions.send_keys(Keys.RETURN).perform()
        except:
            print("[INFO] No need to enter simple_login")
        print("[INFO] Success Login Google")
        return True
    except:
        print("[INFO] Error Login Google")
        return False

