import json
import os

file_name = "my_memo_v2.json"


if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)

else:
    data = {"memo_list": []}

new_memo = input("추가할 메모를 입력하세요 (종료하려면 엔터):")

if new_memo:
    data["memo_list"].append(new_memo)

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


print("\n--- [ 현제 저장된 모든 메모 ] ---")
for i, m in enumerate(data["memo_list"], 1):
    print(f"{i}, {m}")