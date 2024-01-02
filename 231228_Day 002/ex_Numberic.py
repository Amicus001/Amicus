"""
논리연산자; and, or, not
 True/False return
 -and(a and b: a, b all true->True)
 -or(a or b: more than 1 true -> True
 -not(not a: opposite of A; if a(true) =False, a(false)= True  ==>토글(toggle)
"""

no1 = 10
no2 = 4

# and

print(no1 > no2, no1 > 100)
print(no1 > no2 and no1 > 100)
print(no1 > no2 and no1 > 100 and no1 > 1)

# or
# 하나 이상만 True=> True
print(no1 > no2, no1 > 100)
print(no1 > no2 or no1 > 100)
print(no1 > no2 or no1 > 100 or no1 > 1)

# not
# true->False, False-> True
# false = 0, True = 1

print(not False, not True)
print(not 0)  # True 반환
print(not 2, not -3, not 0.0)  # false 반환: 0이 아닌 모든 값을 True로 취급, not True = False

'''
객체비교연산자(is, is not)= True/False 반환
-is; A is B: A,B가 동일한 데이터 타입의 객체인지 여부
-not is; A is not B: A,B가 서로 다른 데이터 타입의 객체인지 여부.
'''

print(f'10 is 10=>{10 is 10}, {10==10}')
print(f'10 is 10.0=>{10 is 10.0}, {10==10.0}')

# 실습

n1 = int(input("숫자를 입력하세요: "))
n2 = int(input("숫자를 입력하세요: "))

# 1
print(f'{n1}+{n2} = {n1+n2}')
print(f'{n1}-{n2} = {n1-n2}')
print(f'{n1}*{n2} = {n1*n2}')
print(f'{n1}/{n2} = {n1/n2}')
print(f'{n1}//{n2} = {n1//n2}')
print(f'{n1}%{n2}={n1%n2}')
print(f'{n1}**{n2} = {n1**n2}')

# 2
print(f'{n1}>{n2} => {n1>n2}\n {n1}<{n2} => {n1<n2}\n {n1}>={n2} => {n1>=n2}\n '
      f'{n1}<={n2} =>{n1<=n2}\n {n1}=={n2} =>{n1==n2}\n'
      f'{n1}!={n2} = > {n1!=n2}')

# 3
maximum = int(input("최댓값:"))
minimum = int(input("최솟값: "))

print(f'{n1}>{n2} and {n1}>{maximum} => {n1>n2 and n1>maximum}')
print(f'{n1}>{n2} and {n1}>{minimum} => {n1>n2 and n1>minimum}')
print(f'not {n1} => {not n1}')
