import hashlib
import json
import os


def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def load_data():
    if os.path.exists('users.json'):
        with open('users.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(users):
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def register():
    users = load_data()
    uid = input("ID: ")
    upw = input("PW: ")
    uname = input("NAME: ")

    users.append({
        "id":uid,
        "password": hash_password(upw),
        "name": uname
    })
    save_data(users)
    print(f"Registered: {uname}")

def login():
    users = load_data()
    uid = input("ID: ")
    upw = input("PW: ")

    hashed_input = hash_password(upw)

    for user in users:
        if user['id'] == uid and user['password'] == hashed_input:
            print(f"Login Success: {user['name']}")
            return
    print("Login Failed")

if __name__ == "__main__":
    while True:
        menu = input("\n1.Reg 2.Login 3.Exit: ")
        if menu == '1': register()
        elif menu == '2': login()
        elif menu == '3': break

