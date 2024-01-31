#람다 함수(람다 표현식)
#익명함수. 짧은 코드의 함수/반복해서 재사용이 많지 않은 코드의 경우 표현
#문법: lambda 매개변수1, 매개변수2, ..., 매개변수n:표현식
#결과: 매개변수를 활용한 표현식 결과값이 lambda 위치에 반환됨.

def add(a,b):
    return a+b

def munus(a,b):
    return a - b

print((lambda a,b:a+b)(4,5 ))
print((lambda a,b: a-b)(4,5))

my_add = lambda a, b: a+b
my_minus = lambda a,b: a-b