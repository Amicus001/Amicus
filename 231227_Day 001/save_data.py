"""
데이터를 메모리에 저장하는 방법
파이썬 문법;  변수명  = 저장할 데이터
python의 변수는 힙 영역에 저장된 데이터의 주소를 저장하는 변수.(=참조변수, 레퍼런스 변수)
"""

#나이(정수, int->hip area)를 메모리에 저장
age = 25

#이름(문자열, str ->hip area)을 메모리에 저장
# Injeolmijeolim 데이터가 저장된 주소를 name 이름이 붙은 메모리에 저장함.
name = "InjeolmiJeolim"

#데이터 주소를 확인하는 내장함수: id( 실제 저장된 데이터 )/ id( 변수명 )

print(id(name))
print(id("InjeolmiJeolim"))

name = "asdf"

print(id(name))

#변수가 저장하고 있는 데이터의 종류(Data type)를 알려주는 함수, type(data / variable)

print(type(3308))
print(type(4.))
print(type("asdf"))
