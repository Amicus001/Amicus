#-----------------------------------------------------
#함수와 클래스
#------------------------------------------------------
#변수에 어떤 데이터를 저장하고 있는지 확인하는 함수;type(variable)

data = 1
print(f'data type= {type(data)}')

data = "good"
print(f'data type= {type(data)}')


#함수명 type
print(f'id()type; {type(id)}')

#사용자 정의 함수--------------------------------------------
#기능: 정수 2개를 더한 후 결과를 출력함
#이름: addTwo
#parameter: n1,n2
#return: 없음

def addTwo(n1,n2):
    print(n1+n2)

#함수 타입 출력;내장함수 type()
print(type(addTwo))

#----------------------------------------------------------------
#함수와 변수
# -함수명은 코드의 시작 주소를 저장하고 있음.
# -함수명 변수에 대입 가능
#-----------------------------------------------------------------
test=addTwo
print(f'test = {id(test)}, {type(test)}')
print(f'addTwo = {id(addTwo)}, {type(addTwo)}')

#-------------------------------------------------------------------
#활용 예시
#1 - 10 범위 내의 임의의 정수 5개 지정(중복 가능)
#---------------------------------------------------------------

import random
num = []
for cnt in range(5):
    num.append( random.randint(1,10))


#5개의 정수에서 최댓값, 최솟값, 내림차순 정렬된 값 결과 출력하기
print(f'최댓값 : {max(num)}')
print(f'최솟값 : {min(num)}')
print(f'합계 : {sum(num)}')
print(f'정렬 : {sorted(num, reverse=True)}')
print(f'개수 : {len(num)}')


funs = {max, min, sorted, sum, len}
for f in funs:
    if f==sorted:
        print(f(num, reverse=True))
    else:
        print(f(num))

fundict = {'최댓값':max, '최솟값':min, '정렬':sorted, '합':sum, '개수':len}
for k,v in fundict.items():
    if k=='정렬':(f'{k}:{v(num, reverse=True)}')
         print(f'{k}:{v(num)}')

    