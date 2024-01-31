def print_hello():
    hello = print("Hello!")

    def print_message():
        msg = hello+"^-^"
        print(hello)



def a():
    x = 10 #함수 a의 지역변수
    def b():
        nonlocal x
        x=20 #함수 b의 지역변수

    b()
    print(x)

#호출
a()