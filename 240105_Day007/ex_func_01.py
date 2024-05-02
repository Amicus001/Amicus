# 함수(function)
# 특정 기능의 구현을 위한 코드의 묶음.
# 자주 사용하는 기능을 함수로 구현한다.
# 문법
# def 함수이름(매개변수, 2,3,4,...):
#   실행코드
#   코드2
#   return 반환값(결과값)
# ==================================
# 기능: 두 개의 숫자의 합을 계산 후 결과를 반환해 줌.
# 이름: addTwo
# 매개변수: x, y
# 반환값: 합계

def addTwo(x, y):
    value = x+y
    return value


# 기능: 두 개의 숫자의 합 계산 후 결과 반환
# 이름: multi
# 매개변수 : x, y
# 반환값: 곱셈결과.

def multi(x,y):
    value = x * y
    return value

# 함수 사용(호출):
# -> 함수 이름(데이터, 데이터)

print(addTwo(1,5))
addTwo(5,2)
addTwo(10,33)

