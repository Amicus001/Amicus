"""
표준입력기능의 내장함수 "input()"
: input("요청메시지")
 ->입력받은 데이터를 str(문자열)로 인식
"""
#이름 입력 받기
name = input("이름을 입력하세요: ")

#입력된 데이터 출력하기
print(f'당신의 이름은 {name}입니다.')
print("당신의 이름은 %s입니다." %name)

#나이 입력받기
age = input("나이를 입력하세요: ")
#입력받은 나이와 데이터 타입 출력
print(age, type(age))

#숫자 2개 입력 받기
n1 = input("정수를 입력하세요: ")
n2 = input("정수를 입력하세요: ")
print(n2, type(n2))

#str-> int 형변환(typeCasting)
    #str(data): 데이터를 문자열로 형변환
    #int(Data): 데이터를 정수로 형변환
    #float(data): 데이터를 실수로 형변환
    #bool(data): 데이터를 bool(참/거짓 판별)로 형변환

    #입력받은 정수 2개를 정수로 타입 변환
n1=int(n1)
n2=int(n2)

print(n1, type(n1))
print(n2, type(n2))

#사칙연산 계산하기
#+(더하기), -(빼기), *(곱하기), **(거듭제곱) /(나누기), //(몫연산), %(나머지연산)
sum = n1+n2
print(f'{n1}+{n2}는 {sum}입니다.')
print(f'{n1}-{n2}는 {n1-n2}')
print(f'{n1}*{n2}는 {n1*n2}')
print(f'{n1}/{n2}는 {n1/n2}')
print(f'{n1}//{n2}는 {n1//n2}')
print(f'{n1}%{n2}는 {n1%n2}')
print(f'{n1}**{n2}는 {n1**n2}')