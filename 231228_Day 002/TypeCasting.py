"""
TypeCasting: '형변환'. 어떠한 자료형을 다른 자료형으로 변환하는 것.
(정수->실수, 실수->문자열, 문자열->논리 등)
-함수: 데이터타입명()
 int(정수)
 float(실수)
 str(문자열)
 bool(논리)
"""

#int(): 정수 타입으로 형변환: 괄호 안에는 10진수 문자만 사용: 문자열 소숫점 사용 불가!

print(type(int('200')))#str->int
print(type(int(200.5)))#float->int: 소숫점 아래는 버림: 데이터 손실 발생

#bool->int
#0 = False, 1 = True

print(type(False)(int(False)))

#str->float 변환: 문자열 소숫점 사용 가능
print((type(float('3.4'))), float('3.5'))
print(type(float(35)), float(35))

#int->float

print((type(float(45)),float(45)))
print((type(float(-9),float(-9))))

#bool->float

print(type(float(False)), float(False))
print(type(float(True)), float(True))