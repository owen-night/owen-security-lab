import hashlib
import os

def secure_hash_password(password):
    salt = os.urandom(16).hex()
    salted_password = password + salt
    hash_result = hashlib.sha256(salted_password.encode()).hexdigest()

    return hash_result, salt

pw = "my_strong_password"
hashed, salt = secure_hash_password(pw)

print(f"원본 비밀번호: {pw}")
print(f"생성된 솔트: {salt}")
print(f"솔트가 적용된 해시값: {hashed}")

def verify_password(stored_hash, stored_salt, input_password):
    salted_input = input_password + stored_salt

    new_hash = hashlib.sha256(salted_input.encode()).hexdigest()
    
    return new_hash == stored_hash


print("\n[System] Starting security verification test...")

test_password = "my_strong_password"

if verify_password(hashed, salt, test_password):
    print("SUCCESS: User authentication confirmed.")
else:
    print("FAILURE: Invalid credentials provided.")

if not verify_password(hashed, salt, "wrong_pw_123"):
    print("SECURITY: Unauthorized access blocked successfully.")