"""
튜플(Tuple); 읽기 전용 리스트.
 -저장 이후 수정, 삭제, 추가, 변경 불가.
 -성별, 주민번호, 국가코드 등의 개인정보나 프로그램상에서 변경되면 안 되는 데이터
 -문법; (data1, data2, data3, ..., datan)/data1, data2, data3, ...
        (data1), data1,
"""

Myinfo = ('F', '123456-12345678')
print(f'Myinfo = {type(Myinfo)}, {Myinfo}')

#성별 데이터 읽기
print(f'Myinfo[0] = {Myinfo[1]}')

#1개 원소를 가진 튜플 생성
Mydata = '82',
print(type(Mydata))