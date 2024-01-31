#다양한 함수의 형태: 기본
#------------------------------
#기능: 팩토리얼 계산 후 계산 결과 반환
#       3! = 3*2*1
#이름: ftrial
#매개변수:n1
#반환값: n1이 1이 될 때까지 생기는 정수를 서로 다 곱한 값.

def ftrial(n1):
    if n1 == 0:
       print(f'0! = 1')
    n=1
    for n in range(n1,0,-1):
        print(f'{n} *')
def factorial(x):
    ret = 1 #결과 저장 변수
    if x :
        for n in range(x,0,-1): ret *= n
    return ret

def fxtrial(x):
    strRet = f'{x}! = '
    intRet = 1
    if x:
        for n in range(x,0,-1):
            intRet = intRet * n
            strRet = strRet+str(n)
            strRet = strRet + ('*' if n!=1 else '=')
        #print (strRet, intRet)
            strRet = strRet+str(intRet)
    return strRet