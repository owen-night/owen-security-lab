user_db = {
    "elon": "mars123",
    "tony": "stark77",
    "owen": "night88"
}

def start_v5_system():
    user_id = input("Enter ID: ")
    user_pw = input("Enter PW: ")


    if user_id in user_db:

        if user_pw == user_db[user_id]:
            print(f"Access Granted. Welcome back, {user_id}")
        else:
            print(f"Access Denied. Wrong password.")
    else:
        print("Access Denied. Unkown User.")


start_v5_system()
