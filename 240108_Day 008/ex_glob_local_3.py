#전역변수(Global Variable), 지역변수(Local Variable)
#전역변수:
#   파이썬 파일에 존재하는 변수.
#   파일 내부 모든 곳에서 사용 가능한 변수
#   파일 실행을 종료하면 사라진다
#지역변수:
#함수 안에서만 사용가능한 변수
#함수가 종료되면 변수는 메모리에서 사라짐.
#------------------------------------------------------

#사용자 정의 함수
def currentdate(todays):#년 월 일을 담은 데이터팔일
    print(f'Today: {todays[0]}/{todays[1]:0>2}/{todays[2]:0>2}') #year, month, date = 지역변수
def currentdate2(month, date):
    print(f'Today: {year}/{month:0>2}/{date:0>2}') #year= 전역변수, month, date = 지역변수

def currentdate3(year, month, date,day):
    print(f'Today: {year}/{month:0>2}/{date:0>2},{date}요일') #year, month, date = 지역변수
#전역변수
year, month,date = 2024,2,8
#호출
currentdate3(year, month, date, "Friday")

print(f'year:{year},month:{month}, date:{date}')
#print(f'day = {day}')#지역변수는 함수 밖에서 사용할 수 없다

