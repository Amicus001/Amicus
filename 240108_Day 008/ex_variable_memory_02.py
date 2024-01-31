#참조형 변수 = 데이터 주소 저장
#---------------------------------------
#저장된 데이터와 변수의 타입 관계

num = 12
print(f'num = {id(num)}, {type(num)}')
num1 = []

num2 = [11,22.1]
print(f'num = {id(num2)}, {type(num2)}')
print(f'num[0] = {id(num2[0])}, {type(num2[0])}')

print("===============값 변경=====================")
#리스트 원소 변경
num = 'Happy'
print(f'num = {id(num)}, {type(num)}')
num2[0] = 100
print(f'num2{id(num2)},{type(num2)}')

num1=num2 #리스트를 다른 리스트로 변경
num1[0]=77
print(f'num1{id(num1[0])},{type(num1[0])}')
