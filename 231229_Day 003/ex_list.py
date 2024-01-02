#list자료형의 연산; 산술연산, 비교연산, 멤버연산]
#1~50 사이의 2의 배수로 구성된 리스트 생성
n2 = list(range(2,51,2))

#산술연산; 덧셈과 곱셈
data = n2 + ["a", "b"] #리스트+리스트 = 리스트의 마지막 원소 뒤에 리스트의 원소 더하여 하나의 리스트 리턴
print(data)
#list+str = 불가. 타입캐스팅 필요; str의 요소 하나하나를 리스트의 element 하나씩으로 계산
#list+str-> str(list)+str => 대괄호를 포함한 전체 덩어리를 문자열 취급함

#list*int = int만큼 원소를 반복하여 하나의 리스트로 리턴

#멤버 연산; in/ not in; True/False 반환
print("c"in data)