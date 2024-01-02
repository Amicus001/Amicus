# str데이터와 관련한 내장함수
# 원소/요소(element)의 개수를 알려주는 내장함수 len()

msg = 'christmas2023!'
print(f'len(msg) -> {len(msg)}개')  # 정수/실수 데이터는 길이(원소/요소)를 가지지 않음

# 문자의 코드값 받는 내장함수 ord()
print(ord('a'))

#"Hello" 코드값 출력

h = ord('H')
e = ord('e')
l = ord('l')
o = ord('o')

print(f'"Hello"의 코드값 목록 {bin(h)[2:], bin(e)[2:], bin(l)[2:], bin(l)[2:], bin(o)[2:]}')

#코드->문자 반환 내장함수 chr(코드값)

print(f'코드값 65에 해당하는 문자: {chr(65)}')