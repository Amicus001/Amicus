# range 내장함수: 숫자의 범위를 생성하는 함수
# 범위에 포함되는 숫자 데이터 = 요소(elements), 인덱싱
no = range(20)
print(no)
print(f'nums = {no[0]}, {type(no[0])}')
print(f'nums = {no[-1]}, {type(no[-1])}')
print(len(no))

#맨 처음 5개 원소만 추출
print(f'nums = {no[0:5]}, {type(no[0:5])}')

#range->list
print(f'list(no) = {list(no)}')

#1~100으로 구성된 정수 리스트 구현
nlist = list(range(1,101))
print(nlist)

#range(시작, 끝)
#시작값 기본 = 0;  range(10) ->0~9
#시작값 = 1;      range(1,10) ->1~9
#시작값 = 5;      range(5,10) ->5~9
#기본적으로 1씩 증가; 건너뛰려면 range(시작, 끝, 스킵)