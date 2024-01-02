"""
튜플과 리스트
"""

mydata = (10, 20, ['hong', 30], ("kim", 12))

#튜플의 원소(요소)갯수 확인 함수=> len()

print(f'mydata 원소 수: {len(mydata)}')

#튜플에서 원소(요소) 데이터 읽기
print(f'mydata: {type(mydata[2])}')

#튜플에서 0번째 원소의 데이터 변경
#mydata[2] = 'Ten'  #튜플 2번째 원소 변경-> 지원X
mydata[2][0] = "Park" #['hong', 30] 리스트 접근.

#1-10 범위에서 2의 배수로 구성된 정수 튜플, 5의 배수로 구성된 정수 튜플
two = tuple(range(2,10,2))
five = tuple(range(5,10,5))

print(two + five, two,five, sep='\n')