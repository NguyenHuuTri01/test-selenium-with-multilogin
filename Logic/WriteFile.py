from Models.InfoAccount import NewInfo as Info
from Models.Email import NewEmail as Email

def WriteLinkReview(email, link, src) -> bool:
    try:
        with open(src, "a") as file:
            file.write(f"{email}|{link}\n")
        print("[INFO] Wrote link review")
        return True
    except:
        print("[INFO] Cannot write link review")
        return False
