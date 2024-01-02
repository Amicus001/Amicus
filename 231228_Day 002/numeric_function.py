# 숫자 데이터 관련 내장함수 살펴보기
# 내장함수 =  built in, 기본으로 제공되는 함수.
# 절댓값 반환; abs(숫자데이터)

num = 99
print(f'{num}의 절댓값 = {abs(num)}')

num = -3
print(f'{num}의 절댓값 = {abs(num)}')

# 실수값에서 소수점 이하 자릿수 처리(반올림) 내장함수(round)]
# 지정된 자릿수 바로 아래 자리 반올림

num = 1.23345667788
print(f'{num} -> {round(num,1)}')


# 최댓값/최솟값 찾는 함수: max(), min()
print(f'max(1,2,3) =>{max(1,2,3)}')
print(f'min(9,0,-3)=>{min(9,0,-3)}')

# 거듭제곱을 계산하는 내장함수: pow(a,b)

print(f'pow(2,3) = {pow(2,3)}')
print(f'pow(2,5) =>{pow(2,5)}')

# 숫자 표현방식으로 변환 내장함수
# 16진수 변환:hex(정수)
# 8진수 변환: oct(정수)
# 2진수 변환: bin(정수)

num = 72
numHex = hex(num)
numOct = oct(num)
numbin = bin(num)

print(f'{num}의 16진수 {numHex}, 8진수 {numOct}, 2진수{numbin}')