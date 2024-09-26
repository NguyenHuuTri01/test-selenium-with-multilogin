from Models.ProfileMultiLogin import NewProfile as Profile
from Models.Email import NewEmail as Email
from Models.InfoAccount import NewInfo as Info
import random
import os

root_dir = os.getcwd()
src = rf"{root_dir}\ListFile"

def GetListEmail(src: str) -> list:
    result = False
    listEmail = []
    try:
        with open(f"{src}", 'r') as file:
            lines = file.readlines()
        if lines is not None:
            result = True
        else:
            print("[INFO] File Email empty")
    except:
        print("[INFO] Cannot read file Email")
        result = False

    if result is True:
        for line in lines:
            line.strip()
            detail_Line = line.split("|")
            new_Email = Email(detail_Line[0],detail_Line[1],detail_Line[2])
            listEmail.append(new_Email)
    return listEmail

def GetListProfile(src: str) -> list:
    result = False
    listProfile = []
    try:
        with open(f"{src}", 'r') as file:
            lines = file.readlines()
        if lines is not None:
            result = True
        else:
            print("[INFO] File Email empty")
    except:
        print("[INFO] Cannot read file Email")
        result = False

    if result is True:
        for line in lines:
            line.strip()
            detail_Line = line.split("|")
            new_Profile = Profile(detail_Line[0],detail_Line[1])
            listProfile.append(new_Profile)
    return listProfile

def GetUsernamePassword() -> list:
    result = False
    try:
        with open(rf"{src}\username_password.txt", 'r') as file:
            lines = file.readlines()
        if lines is not None:
            result = True
        else:
            print("[INFO] File Username and Password empty")
    except:
        print("[INFO] Cannot read file Email")
        result = False

    if result is True:
        lines[0].strip()
        detail_Line = lines[0].split("|")
        listUsernamePassword = [detail_Line[0], detail_Line[1]]
        return listUsernamePassword
    else:
        return None

def GetLinkReview() -> list:
    result = False
    try:
        with open(rf"{src}\linkReview.txt", 'r') as file:
            link = file.readlines()
        if link is not None:
            result = True
        else:
            print("[INFO] File Link Review empty")
    except:
        print("[INFO] Cannot read file Link Review")
        result = False

    if result is True:
        return link
    else:
        return None

def GetContent() -> list:
    result = False
    try:
        with open(rf"{src}\content.txt", 'r',encoding='utf-8') as file:
            content = file.readlines()
        if content is not None:
            result = True
        else:
            print("[INFO] File Content empty")
    except:
        print("[INFO] Cannot read file Content")
        result = False

    if result is True:
        return content
    else:
        return None
