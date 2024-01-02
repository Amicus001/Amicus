#str 연산

m1 = "Good"
m2 = "Happy"

#덧셈: str + str만 가능

print(f'm1+m2={m1+m2}')

#뺄셈연산; 지원안됨
#print(f'm1-m2={m1-m2}')

#곱연산: str*int/int*str = str을 int만큼 반복출력
print(f'5*m2= {m1*5}')

#비교연산(>,<,>=,<=,==,!=)
#사전 찾듯이 원소/요소단위로 코드값을 비교하여 출력; 같은 인덱스 값에 있는 문자열의 코드값ㅇㅇ
print(f'H>I = {"H">"I"}')
print(f'"Ha">"HA" = {"Ha">"HA"}')

# 논리연산(and, or, not)
# not 문자열
#str-bool;
# 요소가 0개= false
# 요소가 1개 이상= true
print(not "happy")

#멤버연산자; 원소/요소가 있는 데이터 타입의 경우
# 요소 in 데이터: 요소에 포함되어 있는 경우-> True
# 요소 not in 데이터: 요소에 포함되지 않은 경우 -> True

print(f'"H" in "Happy": {"H" in "Happy"}')
print(f'"H" not in "Happy": {"H" not in "Happy"}')
