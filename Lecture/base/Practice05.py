# 파일 쓰기
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file = score_file)
score_file.close()

# 파일 읽기
score_file = open("score.txt", "r", encoding="utf8")
# 줄별로 읽고 한줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
score_file.close()

# 반복문 사용
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # 내용 종료
        break # 종료
    print(line)
score_file.close()

# list형태
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end = "")
score_file.close()
