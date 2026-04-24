user_db = {"elon": "mars123", "owen": "night88"}

def start_v6_system():
    while True:
        print("\n=== SECURITY PORTAL v6 ===")
        choice = input("1. Login 2. Sign Up 3. Exit : ")

        if choice == "1":

            uid = input("ID: ")
            upw = input("PW: ")
            if uid in user_db and user_db[uid] == upw:
                print(f"[SUCCESS] Welcome, {uid}")
            else:
                print("[FAILED] Access Denied.")


        elif choice == "2":

            new_id = input("New ID: ")
            if new_id in user_db:
                print("[ERROR] ID already exists.")
            else:
                new_pw = input("New PW: ")
                user_db[new_id] = new_pw
                print(f"[SUCCESS] {new_id} is registered.")
        
        
        elif choice == "3":
            print("System Shutdown.")
            break
        else:
            print("Invalid Choice.")


start_v6_system() 
