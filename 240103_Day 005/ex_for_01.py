#===========================
# 1~100 범위에서 2의 배수에 해당하는 정수 리스트 생성
#===========================

list_2 = list(range(2,101,2))
print(list_2)

#시퀀스 데이터 타입에서 원소 요소를 하나씩 빼서 반복 코드 수행: for-in 반복문
# ==============================================================

# strtwo = ''
# for two in list_2:
#     strtwo = strtwo + str(two)

# print(f'strtwo = {type(strtwo)}\n{strtwo}')
strtwo = ''
#리스트 안의 모든 원소를 str타입으로 변환해서 저장하기
range(len(strtwo))
for idx in range(len(strtwo)):
    strtwo[idx] = str(strtwo[idx])

print(f'[AFTER] result = {strtwo}')