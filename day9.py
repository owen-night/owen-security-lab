import json
import os
import hashlib

def verify_password(input_password, stored_hash, stored_salt):
    test_salted_pw = input_password + stored_salt
    new_hash = hashlib.sha256(test_salted_pw.encode()).hexdigest()
    return new_hash == stored_hash

DB_FILE = "users_v2.json"

def secure_hash_password(password):
    salt = os.urandom(16).hex()
    salted_pw = password + salt
    hashed_pw = hashlib.sha256(salted_pw.encode()).hexdigest()
    return hashed_pw, salt

def register_user(username, password):
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            users = json.load(f)
    else:
        users = []


    if any(user['username'] == username for user in users):
        print(f"[Error] '{username}'은(는) 이미 존재하는 아이디입니다.")
        return False
    
    hashed_pw, salt = secure_hash_password(password)

    new_user = {
        "username": username,
        "password": hashed_pw,
        "salt": salt
    }
    users.append(new_user)

    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

    print(f"[SUCCESS] '{username}'님, 보안 가입이 완료되었습니다.")
    return True
def login_user(username, password):
    if not os.path.exists(DB_FILE):
        print("[Error] 가입된 유저가 아무도 없습니다.")
        return False
    
    with open(DB_FILE, "r") as f:
        users = json.load(f)

    user_data = None
    for user in users:
        if user['username'] == username:
            user_data = user
            break

    if not user_data:
        print(f"[Error] '{username}' 아이디를 찾을 수 없습니다.")
        return False
    
    stored_hash = user_data['password']
    stored_salt = user_data['salt']

    if verify_password(password, stored_hash, stored_salt):
        print(f"[Success] 로그인 성공. 환영합니다, {username}님. ")
        return True
    else:
        print("[Fail] 비밀번호가 일치하지 않습니다.")
        return False
    




register_user("owen_dev", "safe_pass_99")

print("\n--- 로그인 테스트 (성공) ---")
login_user("owen_dev", "safe_pass_99")

print("\n--- 로그인 테스트 (비번 틀림) ---")
login_user("owen_dev", "wrong_password")