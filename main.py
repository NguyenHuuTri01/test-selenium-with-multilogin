from Models.Email import NewEmail
from  Models.ProfileMultiLogin import NewProfile
import Logic.MultiLogin_Services as MultiLogin
import Logic.Google_Services as Google
import time
import Logic.OtherWebsite_Services as OtherWebsite
import Logic.ReadFile as ReadFile
import os

ACCOUNT = ReadFile.GetUsernamePassword()
ACCOUNT_USERNAME = ACCOUNT[0]
ACCOUNT_PASSWORD = ACCOUNT[1]

print('username:',ACCOUNT_PASSWORD)
print('password:',ACCOUNT_USERNAME)

root_dir = os.getcwd()
src = rf"{root_dir}\ListFile"

listEmail = ReadFile.GetListEmail(rf"{src}\listEmail.txt")
if listEmail is not None:
    email = listEmail[0]

listProfile = ReadFile.GetListProfile(rf"{src}\listProfile.txt")
if listProfile is not None:
    profile = listProfile[0]

linkReview = ReadFile.GetLinkReview()
if linkReview is not None:
    link = linkReview[0]

getContent = ReadFile.GetContent()
if getContent is not None:
    content = getContent[0]

print(email)
print(profile)

driver = MultiLogin.Start(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, profile)
driver.maximize_window()
if driver is not None:

    resultLogin = Google.GG_Login(driver, email)
    time.sleep(1)
    # resultLogin = True
    if resultLogin is True:
        OtherWebsite.Auto_Review_No_Image(driver, link, content, email.email)
        time.sleep(2)
        OtherWebsite.Sign_Out_Windows(driver)

    time.sleep(5)
    MultiLogin.Stop(profile)