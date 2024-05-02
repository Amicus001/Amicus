#1 - 10
#'something' <문자열

data = [1,2,3,4,5,6,7,8,9,10]

for a in data:
    print(a)


if a>0:
    print(a)
    print(a)
    if a%2:
        print("Odd")

print ("ok")
print("end")

num = [1,2,3,4,5,6,7,8,9,10]

for n in num:
    print(n, end=' ' if n != 5 else '\n')
print()
# *출력(삼각형으로)

for a in range(1,6):
    print("*" * a)

for a in range(6,0,-1):
    print("*" * a)