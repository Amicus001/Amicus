# str 전용의 함수(메서드;method) 살펴보기
# 메서드 = : 특정 데이터 타입에서만 사용 가능한 함수
# 변수명.메서드이름()/데이터.메서드이름()
# ex: msg = fck
#     msg.method()
#     fck.method()

# str 대문자 변환; upper()
print("fuxkmylife".upper())
# str 소문자 변환; lower()
print("FUXKMYLIFE".lower())

# str이 모두 대문자인지/소문자인지  검사 후 결과 반환; isupper()/ islower()
print("DATA".isupper())
print("data".islower())

# str이 모두 10진수로 이루어져 있는지 검사 후 결과 반환; isdecimal()
print("good".isdecimal(), "0012".isdecimal(), "-9".isdecimal())

# str이 모두 문자로만 구성되어있는지 검사 후 반환; isalpha()
print("god".isalpha())

#str이 문자와 숫자로만 구성되어 있는지 검사후 반환; isalnum()
print("something something 5342".isalnum())

#문자열이 특정 문자(열)로 시작하는지/끝나는지 검사 후 결과 반환
print("???idk".startswith("???"))
print("flower.jpg".endswith("jpg"))

#str 특정 인덱스 문자를 변경하는 메서드; replace()
name = "Hongkilldong"
#k->i 변경; 인덱싱 미지원->메서드 제공
print(name.replace("k","g"))

