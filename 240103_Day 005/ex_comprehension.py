# a list의 원소값을 제곱한 값을 원소로 가지는 blist를 생성

alist = [1,2,3,4]
blist = []

#general for
for a in alist:
    blist.append(a**2)
print(f'alist: {alist} -> blist: {blist}')

# list comprehension
clist = [a**2for a in alist]

# a list 중 짝수인 원소값을 제곱한 값을 원소로 가지는 blist를 생성
for a in alist:
    if a%2==0: #if not a%2:
        blist.append(a**2)


#comprehension
clist2 = [a**2 for a in alist if not a%2]
#        ----  -------------- ----------
#         (3)       (1)         (2)
#(2)가 True인 경우에만 (3) 실행

#3 짝수인 데이터는 제곱, 홀수인 데이터는 그대로 저장한 값을 원소로 가지는 blist 생성
blist3 = []
for a in alist:
    if not a%2:
        blist3.append(a**2)
    else:
        blist3.append(a)
print(blist3)

# dictionary comprehension
blist3 = {a:a**2 if not a%2 else a for a in alist}
#        ----- ---------- ------ --------------
#         (3-T)     (2)   (3-f)         (1)
print(f'blist = {blist3}')