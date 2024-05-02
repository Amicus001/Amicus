#continue: 계속해서.
# 키워드 아래 코드 실행 안 됨
# 반복문 상단으로  이동
#1-30의 리스트 생성

numlist = list(range(1,31))

#짝수만 출력하기

for data in numlist:
    if data%2 == 0:# if not data%2:
        print(data)

for data in numlist:
    if data%2:
        continue
    print (data)


#같은 문제 while문 써서 해결하기
idx = 0
while idx<30:
    if numlist[idx]%2 == 0:
        print(f'{idx}번째 요소: {numlist[idx]}')
    idx += 1

idx = 0
while idx<30:
    if numlist[idx]%2:
        continue
        print(f'{idx}번째 요소: {numlist[idx]}')
    idx += 1