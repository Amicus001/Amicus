#모듈: 특정 목적의 변수, 함수, 클래스를 하나의 파일에 담은 것
# ex: 수학 관련 변수/함수/클래스: math.py
#     파이썬 기본제공 변수/함수/클래스: builtin.py
# 사용: import모듈
#      모듈.변수
#      모듈.함수

#사용하고 싶은 변수, 함수, 클래스 모듈 포함

import random #임의의 수를 추출해주는 변수/함수/클래스
import math #수학 관련 변수/함수/클래스 있는 모듈

#모듈 안에 있는 함수 사용하기
print(math.pi)
print(math.factorial(5))

print(random.random())

for cnt in range(10):
    print(random.random())

#0.0 ~ 1.0 사이의 임의의 실수 추출: random().
#1<=10 정수 추출
for cnt in range(10):
    print(int(random.random()*10)+1)

#randint 함수: a<=~<=b사이의 정수 추출
for cnt in range(10):
    print(random.randint(1,10),end=" ")

lotto = []
End_Point = 11
while True:
    if len(lotto)==End_Point:break
    num = random.randint(1,45)
    if num not in lotto:
        lotto.append(num)

print(f'lotto: {lotto}')