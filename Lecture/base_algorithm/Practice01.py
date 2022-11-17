# k번째 약수 풀이
# n의 약수들 중 k번째로 작은 수 구하기
# 없으면 -1 출력

n = 6
k = 5

result = 0
count = 0
i = 1

while i < n:
    if n % i == 0:
        count += 1
        if count == k:
            result = i
            break
    i += 1

if count == k:
    print(result)
else:
    print(-1)

