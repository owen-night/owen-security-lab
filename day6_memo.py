import json
import os

file_name = "my_memo.json"


if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
        print(f"--- 기존 메모를 불러왔습니다 ---")
        print(f"마지막 메모: {data['content']}")

else:
    data = {"content": "아직 메모가 없습니다."}
    print("--- 새로운 메모장을 생성합니다 ---")


new_memo = input("새로운 메모를 입력하세요: ")
data["content"] = new_memo

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)


print("메모가 안전하게 저장되었습니다.")