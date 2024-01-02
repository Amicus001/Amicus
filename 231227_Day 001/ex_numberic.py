'''
수치 데이터 살펴보기
정수(class int): 양수, 음수, 0
실수(class float): 소수점 있는 거
복소수(class complex)
'''

#[실습] 2개의 정수를 입력받아 비교연산하기.
#       Input() 2개 쓰기, str->int typecast

n1 = int(input("정수를 입력하세요: "))
n2 = int(input("정수를 입력하세요: "))

#비교연산결과 출력

print("%d>%d=>%s" %(n1, n2, n1>n2))
print("%d<%d=>%s" %(n1, n2, n1<n2))
print("%d>=%d=>%s" %(n1, n2, n1>=n2))
print("%d<=%d=>%s" %(n1, n2, n1<=n2))
print("%d==%d=>%s" %(n1, n2, n1==n2))
print("%d!=%d=>%s" %(n1, n2, n1!=n2))