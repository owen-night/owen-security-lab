allowed_users = ["elon", "tony", "peter"]
correct_pw = "001001"

def start_security_system():
    count = 0
    while True:
        user_id = input("Enter ID: ")
        user_pw = input("Enter PW: ")

        if user_id in allowed_users and user_pw == correct_pw:
            print(f"Access Granted. System Online, {user_id}.")
            break
        else:
            count = count + 1
            print(f"Access Denoed. ({count}/3)")

            if count >= 3:
                print("System Locked. Alerting Security Team. ")
                break


start_security_system()