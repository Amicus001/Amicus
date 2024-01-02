# 문자(열) 데이터 살펴보기; str
# 규칙(문법)-> 'data' "data" '''datadatadata''' """datadatadata"""
msg = "Happy new year 2024!"

# 출력
print(msg)

# 문자열의 일부만 추출(발췌)하기: indexing
# left -> right  :  1 2 3 4 5
# right -> left  :  -1, -2, -3,
# 추출: 변수명[인덱스 번호]-> slicing
#      변수[시작: 끝+1: 간격(생략시 1로 취급)]: 여기부터 여기까지 주세요; 연속되거나 규칙 있는 인덱스ㅇㅇ.
print(f'0번 원소 => {msg[0]}')
print(f'1번 원소 => {msg[1]}')
print(f'마지막 원소 => {msg[-1]}')

print(msg[0], msg[1], msg[2], msg[3], msg[4], sep='')
print(msg[-4], msg[-3], msg[-2], msg[-1], sep='')
print(msg[6], msg[7], msg[8], sep='')

# 'happy' 만 출력하기
print(f'msg[0:5]=> {msg[0:5]}')
print(f'msg[-1:-5] =>{msg[-5:20]}')

# 처음부터 슬라이싱하는 경우 시작인덱스 생략 가능
print(msg[:5])

# 끝까지 슬라이싱하는 경우 마지막 인덱스 생략 가능
print(msg[-5:])

# 처음부터 끝까지 자르는 경우
print(msg[:])

#규칙적으로 띄어서 자르는 경우
msg = "123456789"
print(msg[1:8:2])

print(msg[2::3])