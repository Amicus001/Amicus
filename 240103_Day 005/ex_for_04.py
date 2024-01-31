
# ====================
#반복문과 내장함수
# ====================
xlist = ['1', '3', '5', '7']
#
# #xlist 안의 모든 원소를 정수로 변환후 전환
#
# for idx in range(len(xlist)):
#     xlist[idx] = int(xlist[idx])
# print(f'xlist = {xlist}')

# 시퀀스/ 반복 가능한 개체의 요소(원소)에 적용 후 값을 다시 저장하는 경우
# 자주 사용하는 기능, 내장함수로 제공(map())
# map(함수명, 시퀀스/반복가능개체)
# ===============================
#int인 xlist를 str로 변환

# map(str,xlist)

#________________________________________-
# list data -> dict data

x = ['std01', 'std02', 'std03']
y = [90, 100, 99]
#
# xydict = dict()
#
# for index in range(len(x)):
#     xydict[x[index]]==y[index]
#
#3: dict()
# xy = []
# for idx in range(len(x)):
#     xydict = dict(x,y)
#     xy.append(xydict[x[idx]], y[idx])

# print(xy)
#
# xydict3 = dict(xy)

# 내장함수(zip)

xydict4 = dict(zip(x,y))
print(xydict4)