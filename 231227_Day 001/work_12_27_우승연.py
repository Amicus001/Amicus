#1번
hometown = "seoul"
bloodtype = "AB"
season = "winter"
h= 163
phone_number = '01074062925'
country = "Korea"


#2번
mbti = input("MBTI :")
blood = input("blood: ")
gender = input("gender: ")
height = input("height:" )
weight = input("weight: ")

#여러데이터 출력방법
print("[신상 정보]",)
print("MBTI : ", mbti,)
print("혈액형: ", blood,)
print("성별: ", gender,)
print("키: ", height,)
print(" 몸무게:", weight)

#서식지정자 출력방식
print("[신상 정보]")
print("MBTI:, mbti\t혈액형: , blood\t 성별:, gender\t, 키:, height\t, 몸무게:, weight")
#F스트링 출력방식
print(f'MBTI: {mbti}\t 혈액형:{blood}\t 성별:{gender}\t 키:{height}\t 몸무게: {weight}')

#3-1

print("데이터 50, ", type(50))
print("데이터 0.91", type(0.91))
print("데이터 Winter", type('Winter'))
print("데이터 False", type(1+3==2))

#3-2
f_season = input("좋아하는 계절은?: ")
print(f'당신은 {f_season}을 좋아하는 군요!')

eng = input("봄은 영어로?:")
print(f'봄은 영어로 {eng}입니다.')

#4번 문제
"""
힙 영역
스택 영역
"""

#5-1
"""
정수: int
실수: float
글자: str
논리: bool
"""

#5-2
"""
정수 11은 (2진수로) 0b1011
정수 11은 (8진수로) 0o13
정수 11은 (16진수로) 0xb
"""

#6
vertical = int(input("직육면체 가로길이: "))
horizontal = int(input("직육면체 세로 길이: "))
cube_height = int(input("직육면체 높이 길이: "))

area = vertical * horizontal
volume = area * cube_height

print(f'직사각형 넓이: {area}')
print(f'직육면체 부피: {volume}')