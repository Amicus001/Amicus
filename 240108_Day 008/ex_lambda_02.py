#리스트 안의 모든 원소를 더한 합계 출력
datas = [1,4,9]

for idx, d in enumerate(datas):
    datas[idx] = int(d)

print(datas)

#내장함수 map
map(int, datas)

#원소에 100을 곱한 값을 리스트에 저장하기
def multivalue(x):
    return x *100

datas = list(map(multivalue, datas))
print(datas)

def greeting():
    print("hi!")

print((lambda:"hello")())