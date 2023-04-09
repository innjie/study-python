# 대표값 구하기

# N명의 학생의 수학점수 중 평균 (소수자리 반올림), 평균에 가까운 학생은 몇번째인가 확인
import sys
sys.stdin = open("../text_files/Practice06.txt", "r")


n = int(input())
a = list(map(int, input().split()))

ave = round(sum(a) / n + 0.5) # 소수 첫째 자리에서 반올림, python은 round 함수가 round_half_even 방식임
min = 2147000000
score = 0
for idx, x in enumerate(a) : # enumerate : a 탐색 시 idx에 인덱스 값 반환
    tmp = abs(x - ave) # 절댓값(거리)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min: # 최소점수와 현재 점수의 평균차 절댓값이 같은 경우
        if x > score : # 점수 자체의 크기 비
            score = x
            res = idx + 1
print(ave, res)

