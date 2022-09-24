weather = input('weather?')  # 입력 가능
if weather == 'rain':
    print('umbrella')
elif weather == 'wind':
    print('cloth')
else: # 조건문 입력하지 않음
    print('nothing')

for waiting_no in [0, 1, 2, 3, 4]:
    print('waiting No : {0}'.format(waiting_no))

# 같은 동작
for waiting_no in range(1, 6):
    print('waiting No : {0}'.format(waiting_no))

students = [1, 2, 3, 4, 5]
students = [i + 100 for i in students] # [101, 102, 103, 104, 105]

students = ['a', 'aa', 'aaa']
students = [len(i) for i in students]

students = ['a', 'bB', 'ccC']
students = [i.upper() for i in students]

customer = 'aaa'
index = 5
while index >= 1:
    print('{0}, {1]'.format(customer, index))
    index -= 1

    if index == 0:
        print('end')


absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print('{0}'.format(student))
        break

# -----------------------------
# IO
print('python', 'java', sep = ',')

# python, java?
print('python', 'java', sep = ',', end = '?')

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    # subject와 score가 key-value로 나눠서 나온다.
    print(subject, score)

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    # subject와 score가 key-value로 나눠서 나온다.
    print(subject.ljust(8), str(score).rjsut(4), sep = ":")

# 10자리 확보하고 500 출력, 오른쪽 정렬
print("{0: >10}".format(500))
# 부호 출력
print("{0: >+10}".format(500))
# 왼쪽 정령, 빈칸 _로 바꾸기
print("{0:_<+10}".format(500))
# 3자리마다 , 출력
print("{0:,}".format(100000000))
# 소수점 특정 자리수까지만 표시
print("{0:.2f}".format(5/3))