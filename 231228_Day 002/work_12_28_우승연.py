
#1-1
id = "kim1234@naver.com"
print(id[:7])

#1-2
domain = "http://www.naver.com"
print(domain[11:])

#1-3
name = "홍길동"
print(name[1:3])

#1-4
s = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr"
print(s[::2])
print(s[1::2])

#1-5
m = "ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ"
print(m[3::4])

#1-6
id = "881120-1068234"
print(id[:6])
print(id[7:])

#2
n1 = int(input("정수 입력: "))
nOct = oct(n1)
nHex = hex(n1)
nBin = bin(n1)
print(f'정수 입력: {n1}\n16진수: {nHex}\n8진수: {nOct}\n2진수: {nBin}')

#3
word1 = input("입력")
word2 = input("입력")
word3 = input("입력")

print(f'코드 값이 가장 큰 단어: {max(word3,word2,word1)}')
print(f'코드 값이 가장 작은 단어: {min(word2, word1, word3)}')

#4
w = input("단어 입력:")
s1 = "오늘은 행복한 목요일입니다."
print(w, "단어 메시지 존재 여부: ",w in s1)

#5

w1 = input("단어 입력: ")
w2 = ord(w1[0])
w3 = ord(w1[1])
w4 = ord(w1[2])

w2= bin(w2)
w3= bin(w3)
w4= bin(w4)
print(w2, w3[2:], w4[2:])
