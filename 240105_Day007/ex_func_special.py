#특별한 함수 1: 매개변수의 갯수를 유동적(가변)으로 하는 함수
# def 함수명(*data): << "가변인자함수" 매개변수 갯수: 0 ~ n개


#2개의 정수 덧셈 후 반환하는 함수 생성

def add(a,b):
   return a+b

def addFive(a,b,c,d,e):
    return a+ b+ c+ d+ e

def addThree(a,b,c):
    return a+b+c

def addNumber (*data):
    print(type(data))
    ret = 0
    for d in data:
        ret = d+ret
    return ret
#호출

print(addNumber(1,2,3))
print(addNumber(10))
print(addNumber())
print(addNumber(1,2,3,4,5,6,7,8,9,10))

print(addNumber(*range(1,11))) # *시퀀스/반복가능한객체 -> 내부의 모든 원소를 하나씩 풀어서 전달한다: 언패킹

a = [11,22,33,44]
aTuple = 'a','b','c'
print( *a, sep= '-') # **(아스타리스크): key & value