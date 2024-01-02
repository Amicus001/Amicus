# Q. 10명 학생에 대한 학점 저장
#   -학생 이름과 학점
# --------------------------------------------
# S1. 학생이름 변수 10개 + 학점 변수 10개
# S2. 학생 이름 변수 10개 리스트 + 학점 변수 10개 리스트

snumbs = ['std01', 'std02', 'std03', 'std04', 'std05']
scores = [50, 80, 90, 700, 800]


#03번 학생의 학번과 점수 출력하기
idx = snumbs.index('std03')

print(f'{snumbs[idx]}학번 학생의 점수{scores[idx]}')

#dict 자료형

studenscore = {'std01':90, 'std02':52, 'std03':55, 'std04': 50, 'std05': 99}
print(f'studentscore:{len(studenscore)}개 {type(studenscore)}, {studenscore}')


#딕셔너리에 원소 추가하기: 변수명[새로운 키] = 데이터
studenscore['std10'] = 100
print(f'studentscore:{len(studenscore)}개 {type(studenscore)}, {studenscore}')

#딕셔너리 요소 데이터 변경: 변수명[기존 키] = 새로운 데이터

#원소 삭제: del 변수명[key], del(변수명[키])