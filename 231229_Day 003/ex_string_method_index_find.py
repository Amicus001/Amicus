data = "Iwannagohome"
print(data.index('g'))
# 괄호 안에 있는 문자의 인덱스 반환
# 좌--->우 순 가장 먼저 있는 문자의 인덱스 반환

word = "123123123"
print(word.index('1', 3))

first_n = data.index('n')  # 0번 인덱스부터 하나씩 검사하여 ()안에 해당하는 인덱스 찾기
sec_n = data.index('n', first_n+1)  # 첫번째 n 인덱스 이후 원소부터 검사하여
print(data.index('n', first_n)+1)


#! 의 인덱스를 찾기
#print(data.index('!')) #존재하지 않는 문자열 인덱스=>ValueError 발생


# str데이터에서 특정 문자의 인덱스를 반환하는 메서드: find()
# index()와 다르게 괄호 안의 문자열이 문자열 데이터 안에 없으면 -1 반환

print(data.find('!'))