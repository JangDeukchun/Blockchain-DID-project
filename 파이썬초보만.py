# print("강아지" + "고양이")
# print("반가워요" * 20)
# print("100" + "200")
# print(100 + 200)

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# t.forward(100)
# t.left(90)
# t.forward(50)
# t.right(90)
# t.forward(100)

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

# print("안녕 한동근")
# print("프로그래밍 공부를 즐기셨으면 합니다")
# print("안녕" *3 )

# import turtle

# colors = ["red", "purple", "blue", "green" "yellow", "orange"]
# t = turtle.Turtle()

# turtle.bgcolor("black")
# t.speed(0)
# t.width(3)
# length = 10

# while length < 500:
#     t.forward(length)
    
#     44번째줄 오류 이유 모르겠음t.pencolor(colors[length%6])
#     t.right (89)
#     length += 5

# x = 100
# x = 200
# y = 300 
# sum = x + y
# print(sum)

# name = "홍길동"
# address = "서울시 종로구 1번지"

# print(name)
# print(address)
 
# x = 100
# y = 200
# sum = x + y

# print( x, "과", y, "의 합은", sum, "입니다" )

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# radius = 100
# t.circle(radius)
# t.fd(30)
# t.circle(radius)
# t.fd(30)
# t.circle(radius)
# t.fd(30)

# x = int(input("첫 번째 정수를 입력하시오: "))

# print(x)30

# x = int(input("첫 번째 정수를 입력하세요:"))
# y = int(input("두 번째 정수를 입력하세요:"))
# sum = x + y
# print(x, "와", y, "의 합은", sum, "입니다")

# name = input("이름을 입력하세요 : ")
# print(name)






# 거북이로 집 그리기

# 터틀 그래픽을 사용하여야 하므로 다음과 같은 코드를 소스 파일에 입력한다
# import turtle
# from typing import Sized
# t = turtle.Turtle()
# t.shape("turtle")

# # 사용자로부터 집의 크기를 받아서 size라는 변수에 저장한다
# # 집의 크기는 정수이므로 input()이 반환하는 문자열을 int()를 통하여 정수로 변환한다
# size = int(input("집의 크기는 어마로 할까요?: "))

# # 집을 그릴 차례이다. 사각형을 다음과 같은 코드로 그린다. 이때 변수 Size를 사용하자
# t.forward(size) # 사이즈만큼 거북이를 전진시킨다
# t.right(90) # 거북이를 오른쪽으로 90도 회전시킨다
# t.forward(size)
# t.right(90)
# t.forward(size)
# t.right(90)
# t.forward(size)

# # 이제 지붕을 그릴 차례이다. 현재 거북이는 위를 보고 있기 때문에 
# # 거부그이를 오른쪽으로 90도 회전시켜서 오른쪽을 보도록 한다.
# t.right(90)

# # 지붕을 그리면 된다. 지붕은 간단히 삼격형으로 그렸다.
# t.forward(size)
# t.left(120)
# t.forward(size)
# t.left(120)
# t.forward(size)
# t.left(120)

# 로봇 기자 만들기
# stadium = input("경기장은 어디입니까? : ")
# winner = input(" 승리팀은 어디입니가? : ")
# loser = input(" 패배팀은 어디입니까? : ")
# mvp = input( " 우수 선수는 누구입니까? :")
# score = input("스코어는 무엇입니까? : ")

# 변수와 문자열을 연결하여 기사를 작성한다
# print("")
# print("=======================")
# print("오늘", stadium, "에서 경기가 열렸습니다")
# print(winner, "와", loser, "는 치열한 경기를 평쳤습니다")
# print(mvp, "가 맹활약을 펼쳤습니다")
# print(winner, "가", loser, "를", score, "로 이겼습니다")
# print("=========================")

# print(7/4)
# print(7//4)

# p = int(input("분자를 입력하세요"))
# q = int(input("분모를 입력하세요"))

# print ( p // q )
# print ( p % q)

# sec = 100
# min = 1000 // 60
# remainder = 1000 % 60
# print(min, remainder)

# 거북이를 이용해서 다각형 그리기

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# n = int(input( "몇각형을 그리시겠어요? :" ))

# for i in range(n) :
#     t.forward(100)
#     t.left(360//n)

# 자동 판매기 프로그램

# money = int(input("투입한 돈: "))
# price = int(input("물건 값: "))

# change = money - price
# print("거스름돈 :", change)
# coin500 = change // 500
# change = change % 500
# coin100 = change // 100

# print("500원 동전 개수 :",  coin500)
# print("100원 동전 개수 :", coin100)

# 지수 연산자는 다른 연산자보다 우선순위이다
# 원리금 합계를 복리로 계산하는 식을 만들어 보자

# 원금
# a = 

# 이자율
# r = 

# n년 후에 원리금 합계 
# b = a(1+r)^n

# a = 1000
# r = 0.05
# n = 10

# print(a*(1+r)**n)

#대입 연산자
# x = 100 + 200
# x = y = 100

#복합연산자

# num = num + 2

# num += 2

# x +=y = x = x + y

# x -=y = x = x - y   

# x *=y = x = x * y

# x /=y = x = x / y

# x %=y = x = x % y



# 숫자를 문자로 변환하기 

# print('나는 현재' + str(21) + '살이다' ) 

# price = 10000

# print("상품의 가격은 %s원 입니다" % price)

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("", "이름을 입력하시오: ")
# t.write("안녕하세요" + s + "씨 인사 드립니다")

# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)

# s = "monty python"
# print(s[6:10])

# message = 'doesn\'t'
# print(message)

# 2050 년에는 몇살이 될까 ?

# import time

# now = time.time()

# thisyear = int(1970 + now //(365*24*3600))

# age = int(input("몇살이세용:"))
# print(thisyear)

# print(age + (2050 - thisyear))

# 리스트 : 여러 개의 자료들을 모아서 하나의 묶음으로 저장 할 수 있다.

# slist = ['영어', '수학', '사회', '과학']

# list1 = [1,2,3,4,5,6]

# list2 = ['a','b','c','d']

# print(slist)

# list.append 함수 = 빈 리스트 안에 값을 추가하는 함수입니다.

# list = []
# list.append(1)
# list.append(3)
# list.append(4)
# list.append(5)
# list.append(6)
# list.append(7)

# print(list)

# 리스트 값 출력하기
# slist = ['서현식', '황기운', '한동훈', '한동근', '강기모']
# print(slist[0])

# 예제 친구들의 리스트 생성하기
# friend_list = []

# friend = input('친구의 이름을 입력하시오: ')
# friend_list.append(friend)
# print(friend_list)

# 리스트에 저장 된 색상으로 거북이 원 그리기

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# # 리스트를 사용하여 문자열을 저장한다

# color_list = [ "yellow", "red", "blue", "green"]

# t.fillcolor(color_list[0]) # 채우기 색상
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.forward(50)
# t.fillcolor(color_list[1]) # 채우기 색상
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.forward(50)
# t.fillcolor(color_list[2]) # 채우기 색상
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.forward(50)
# t.fillcolor(color_list[3]) # 채우기 색상
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# 우리가 프로그램을 작성 할 때 사용 할 수 있는 3가지의 기본 제어 구조가 있다

# 순차구조 - 명령들을 순차적으로 실행하는 구조
# 선택구조 - 둘 중의 하나의 명령을 선택하여 실행되는 구조이다.
# 반복구조 - 동일한 명령이 반복되면서 실행되는 구조이다

# 1. 선택구조 
# 선택주ㅗ는 질문 한 후에 결정을 내리는 것이다
# (ex) 게임에서 이긴 철수  점수 1 증가
#      파일이 디스크에 없으면 오류 출력 등


# score = int(input("성적을 입력하세요: "))
# if score >= 60:
#     print("합격입니다")
#     print("서현식입니다")
# else:
#     print("불합격입니다")
    
# num = int(input("정수를 입력하세요:"))

# if num % 2 == 0 :
#     print("짝수입니다")
# else:
#     print("홀수입니다")

# 정수 부호에 따라 거북이를 움직이자

# import turtle
# t= turtle.Turtle()
# t.shape("turtle")

# t.penup() # 펜을 올려 그림이 그려지지 않게 한다
# t.goto(100 ,100)
# t.write("거북이가 여기로 오면 양수 입니다")

# t.goto(100 ,0)
# t.write("거북이가 여기로 오면 0 입니다")

# t.goto(100 ,-100)
# t.write("거북이가 여기로 오면 음수 입니다")

# t.goto(0,0) # 이 좌표로 거북이를 이동시킨다
# t.pendown() # 펜을 내려서 그림이 그려지게 한다
# s  = turtle.textinput("", "숫자를 입력하시오 :")

# n =int(s)

# if( n>0):
#     t.goto(100,100)
# if (n == 0):
#     t.goto(100,0)
# else:
#     t.goto(100,-100)

# 거북이  제어하기
# l 입력하면 왼쪽으로 100픽셀 이동 r 누르면 오른쪽으로 100픽셀 이동한다
# 반복문을 이용한다

# import turtle
# t =turtle.Turtle()
# t.width(3) 
# t.shape("turtle")  # 커서 모양을 거북이로 한다
# t.shapesize(3,3)

# while True:
#     a = input("명령어를 입력하시오: ")
#     if a == "l":
#         t.left(90)
#         t.forward(100)
#     if a == "r":
#         t.right(90)
#         t.forward(100)

# 윤년만들기 
# year = int(input("년도를 입력하세요:"))

# if ((year % 4 ==  0 and year % 100 != 0) or year % 400 == 0):
#     print(year, "년은 윤년입니다.")

# else :
#     print(year, "년은 윤년인 아닙니다.")

# 동전 던지기 게임

# import random
# coin = random.randrange(2)
# if coin == 0:
#     print("앞면입니다")
# else:
#     print("뒷면입니다")
# print("게임이 종료되었습니다.")


# num = int(input("정수를 입력하시오: "))

# if num > 0 :
#     print("양수입니다")
# elif num == 0 :
#     print("0입니다")
# else:
#     print("음수입니다")


# 종달새가 노래할까 ?

# import random
# time = random.randint(1, 24)
# sunny = random.choice([True,False])
# if sunny:
#     print("날씨 좋음")
# else:
#     print("날씨 안좋음")

# if time >=6 and time <9 and sunny:
#     print("종달새가 노래합니다")
# else:
#     print("종달새가 노래하지 않습니다")


# 팁 : random.randint 는 a가 최소 b가 최대의 범위가 된다
#     random.randrange는 a가 최소 b-1가 최대의 범위가 된다

# 중첩 if문
# num = int(input("정수를 입력하세요 "))
# if num >= 0:
#     if num == 0:
#         print("0입니다")
#     else:
#         print("양수입니다")
# else:
#     print("음수입니다")

# 아이디 확인
# id = rldns3457
# s = input("아이디를 입력하세요")
# if id == s:
#     print("환영합니다")
# else:
#     print("아이디를 찾을 수 없습니다")

# 패널티킥
# import random

# option = ["왼쪽", "가운데", "오른쪽"]
# computechoice = random.choice(option)

# userchoice = input("어디를 수비하시겠어요 ?")

# if computechoice == userchoice:
#     print("수비성공")
# else:
#     print("성공")


# 도형 그리기
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("","도형을 입력하세요 :")
# if s == "사각형":
#     s = turtle.textinput("", "가로:")
#     w = int(s)
#     s = turtle.textinput("", "세로")
#     h = int(s)
#     t.forward(w)
#     t.left(90)
#     t.forward(h)
#     t.left(90)
#     t.forward(w)
#     t.left(90)
#     t.forward(h)
    