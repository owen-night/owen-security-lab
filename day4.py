allowed_users = ["elon", "tony", "peter"]
correct_pw = "001001"

def check_security():
    user_id = input("Enter ID: ")
    user_pw = input("Enter PW: ")

    if user_id in allowed_users and user_pw == correct_pw:
        print(f"Access Granted. Welcome, {user_id}.")
        return True
    else:
        print("Access Denied.")
        return False

check_security()