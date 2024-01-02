"""
출력 내장함수 print()
"""

#1개 데이터 화면에 출력
print("asdf")

#2개
print("asdf", "the air")
print(100, "no me gusta el pepino")

#여러 데이터를 화면에 출력할 때
print("asdf", 5, 3.141592, "Muffin time")

#데이터가 없는 경우 화면 출력
print()

#조금 더 편리한 데이터 출력 방법
    #문자열+숫자(대부분)
#example: [출력] "오늘은 2023년 12월 27일입니다."

print("오늘은 2023년 12월27일입니다.")

year = 2023
month = 12
date = 27

print("오늘은", year,"년", month,"월",date, "일입니다." )

#변수를 str에서 적용하여 출력하기----01.  '%알파벳 한 개' : 서식 지정자 방식
                                #    %d(10진수 정수) '당신은 %d세입니다.'  %age(변수)
#                                    %f(실수),      '평균 %s점입니다.'   %avg
#                                    %s(문자열)      '당신은 &s출신입니다.' %name

age = 25
avg = 99.71
name = 'dantalian'

print('당신은 %d입니다.' %age)
print('평균 점수는 %f점입니다.'%avg)
print('your name is %s with D.'%name)

print('you are %d, average points are %f, name is %s.'%(age, avg, name))

#변수를 str에서 적용하여 출력하기----02. f'{변수}' : f-string

print(f'your age is {age}.')
print(f'the average points are {avg}.')
print(f' your name is {name}.')

print(f' you are {age}years old, average points are {avg}, and your name is {name}.')

print("-"*60)
"""
[실습 1] 본인 이름, 전공, 나이를 메모리에 저장하기.
        저장된 정보를 다음과 같은 형태로 출력하기.
        이름: 홍길동
        전공: 체육학과
        나이: 21세
"""

name = "우승연"
major = "스페인어중남미학전공"
age = 25

# print(f'이름: {name}',)
# print()
# print(f'전공: {major}',)
# print()
# print(f'나이: {age}')

#escape문자: 특별한 의미를 가지는 문자 조합, /알파벳1개 구성
#\n(줄바꿈), new line
#\t(들여쓰기) tab키(4칸 공백)만큼 간격
print(f'이름: {name}\n 나이:{age}\n 전공: {major}')

#print()함수에서 여러 데이터를 분리하여 출력하는 법
    #기본: 공백
    #변경: sep (매개변수): 여러 개의 데이터를 보기 편하게 분리하는 방법 설정

print("홍", "길동","의적")

print("홍","길동", "의적",sep='')

#print()함수에서 데이터화면 출력 후 끝에 추가하는 문자 지정
    #기본: 줄바꿈 이스케이프문자 \n
    #변경: end매개변수; 화면출력 후 원하는 문자 지정 가능.

print("A", end="")  #"A"
print("B", end="")  #"B"
print("C")          #"C"\n

#실습
#다음과 같이 출력되도록 코드를 작성합니다
#  ABCDEFG
#  123456789
#  ABCEDFG

print("ABCDEFG\n 123456789\n,ABCDEFG") #escape 문자 사용
print("ABCEDFG", 123456789, "ABCDEFG", sep='\n') #print()함수의 sep'\n' 사용