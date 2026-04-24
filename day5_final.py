user_db = {
    "elon": "mars123",
    "tony": "stark77",
    "owen": "night88"
}

def start_v5_final():
    print("================================")
    print("    SECURE ACCESS TERMINAL v5   ")
    print("================================")

    input_id = input("Enter Terminal ID: ")
    input_pw = input("Enter Security PW: ")

    if input_id in user_db:

        if input_pw == user_db[input_id]:
            print(f"\n[SUCCESS] Welcome, {input_id}. System Access Granted.")
        else:
            print(f"\n[FAILED] Warning: Incorrect password for {input_id}.")
    else:
        print(f"\n[ALERT] Unknown User: '{input_id}' tried to access.")


start_v5_final()
