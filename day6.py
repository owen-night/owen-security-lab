import json


progress = {
    "day": 6,
    "user": "Owen",
    "status": "Lerning File I/O",
    "note": "파일 저장 기능을 배우고 있습니다."
}

progress["next_step"] = "데이터 불러오기 실습"


file_name = "my_progress.json"

with open(file_name, "w", encoding="utf-8") as f:
    
    json.dump(progress, f, indent=4, ensure_ascii=False)

print(f"'{file_name}' 파일이 현재 폴더에 생성되었습니다.")




with open(file_name, "r", encoding="utf-8") as f:

    loaded_data = json.load(f)

print("\n--- 저장된 파일을 다시 일어온 걀과 ---")
print(f"불러온 데이터: {loaded_data}")
print(f"반가워요, {loaded_data['user']}님. {loaded_data['day']}일차 공부도 화이팅입니다.")
          




