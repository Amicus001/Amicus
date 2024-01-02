# 키보드로 숫자를 입력받아 입력받은 숫자만큼 * 출력
# 1. 숫자 입력 받기
# 2. 입력받은 숫자만큼 * 출력하기 -> 문자열 곱셈.('*'*int)


#입력받은 문자가 있을 경우 = len(num)


num = input("숫자를 입력하세요:")
if len(num)>0:
    num1 = int(num)
    print("*" * num1)

else:
   print("정수를 입력해 주세요. ")

print("END")