# str데이터에서 특별한 의미를 가지는 문자 = 이스케이프 문자
#   \문자, \알파벳(1개)
#   \n(줄바꿈), \t(tab간격), \'(인용), \"(인용), \u(유니코드), \\(경로:파일/주소의 경로)

print('Happy new year 2024~!')
print('Happy new \'year\' 2024~!')
print("Happy new \"year\" 2024~!")

# file 경로
# 파일/데이터 경로일 경우 이스케이프문자 비활성화
# -> r' 경로 ': raw string
print("C:\\Users\\kdp\\Videos\\asdf.py")
print(r'C:\Users\kdp\Videos')