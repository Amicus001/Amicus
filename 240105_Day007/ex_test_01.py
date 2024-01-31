#[실습1] 2개의 정수를 입력받은 후 사칙연산 수행 결과를 반환하는 기능의 함수를 정의하라.

def fourCalc(n1,n2):
    p = n1+n2
    minus = n1-n2
    multify = n1 * n2
    divide = n1/n2 if n2 else 'cannot be divided by 0'

    return p, minus, multify, divide

#[실습2] 문자열을 16진수 코드값으로 변환 후 반환하는 함수를 정의하라.

# def getCode(*message):
#     string = ''
#     string = hex(ord(message))
#     return str(message)

def getcodeA(message):
    ret = ''
    for msg in message:
        ret +=hex(ord(msg))