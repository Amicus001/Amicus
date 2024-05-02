# 매개변수가 존재하지 않는 형태의 함수 (프로그램 버전 출력 기능 등...)
# 매개변수: 함수에게 전달되는 데이터
# def 함수이름():
#   조건코드&리턴값
#   실행코드
#   실행코드
#----------------------------------------
# 함수 기능: 프로그램 정보 출력
# 함수 이름: info
# 매개 변수:
# 반 환 값: str

def info():
    return " MyGame Version 1.0\n Developer IJM \n Email: mastergame@.com"
def welcome():
    print("하이빵가루~")  #누르면 소리 내는 인형...같은 어쩌구임.

welcome()
infomsg = info()
print(infomsg)