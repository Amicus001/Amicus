#매개변수 갯수를 유동적(가변)으로 하는 함수
#키와 값의 덩어리 데이터
#형태: def 함수명(**data):
#가변인자함수
#매개변수는 0 ~ n개
#호출: 함수명(key1 = value1)
#     함수명(key1 = value1, key2 = value2, key3 = value3)
#     함수명()

aDict = {'name':'hong', 'age':18}
aDict.update( status= "student")

#------------------------------------------------------------------------
#기능 : 회원가입기능
#이름 : joinMember
#매개변수: 이름, 전화번호, id, 이메일, 취미, 추소, 생일, etc. -> 가변 + 데이터 정보 (함께)
#       -> 키워드 파라미터 **member
#반환값: '가입 완료되었습니다' str

def joinMemeber(**member):
    print(member)
    members[len(members)+1] = member
    #members.append(member)
    # members.update(**member)
#호출
#가입된 회원 저장 변수
members = {}
#회원가입 기능 함수 호출
joinMemeber(name = 'hong', age = 17, birth = 2010)
joinMemeber(id = "hong84", phone = '0101234134', job = 'actor',blood = 'B')
joinMemeber(id = 'amicus1234', birth = '20240101', blood = 'A')


# 회원가입 2-----------------------------------------------------------------------
#매개변수 필수: id/pw
#       선택: **option 이름 전화, 기타등등

def joinmember2(id, pw, loc = '외국인', gender = '남성', **option): #필수매개변수에 값을 지정해두면 디폴트값이 됩니다.
    print("o")                     # 순서를 신경쓰지 않고 그냥 입력하고 싶을 때는 디폴트 매개변수를 적고서 값을 적어야 함.

joinmember2('h', 'ph', )
joinmember2('h', 'ph', asdf = 'asdf' )

def joinmember3(id,pw,loc = '내국인', gender = '남성', **option):
    print(id, pw, loc, gender, option)
    #key = id, value = pw, loc, gender, **option
    valueDict = {}     # value값을 dict로 제작
    valueDict['pw']= pw
    valueDict['loc']= loc
    valueDict['gender']= gender
    valueDict['etc']= option
    members[id]= valueDict     ## key : id / value : valueDict  # key가 id인 dict의 value 값을 dict로 받음
print(f'[AF]----------------')
for m in members.items():
    print(m)