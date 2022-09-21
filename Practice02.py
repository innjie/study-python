# math method
print(abs(-5))  # 5
print(pow(4, 2)) # 4의 2제곱
print(max(5, 12)) # 12
print(round(3.14))  # 3
print(round(4.59))  # 5

from math import *
print(floor(4.99))  # 4
print(ceil(3.14))  # 4
print(sqrt(16))  # 4

from random import *
print(random())  # 난수 생성
print(randrange(1, 46)) # 1 ~ 46 미만 난수 생성
print(randint(1, 45)) # 1 ~ 45 포함 난수 생성

# Quiz
print(randint(4, 28))

# slicing
userNo = '990120-1234567'

python = 'python is amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)

print(python.find("n"))
print(python.find('java'))  # -1
#print(python.index("Java"))  # error
print(python.count("n"))

# 01.
print("나는 %d살 입니다." % 20)
print('나는 %s를 좋아합니다.' % '파이썬')
print('Apple은 %c로 시작합니다.' % 'a')
print('나는 %s색과 %s색을 좋아합니다.' %('파란', '빨간'))

# 02.
print('나는 {}살입니다.' .format(20))
print('나는 {}색과 {}색을 좋아해요.' .format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요.' .format('파란', '빨간'))  # 반대로 출력

# 03.
print('나는 {age}살이며, {color}색을 좋아해요.' .format(age = 20, color = '빨간'))

# 04.
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')