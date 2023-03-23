# # 1. 자료형 

# # 1- 1. 숫자형, 실수형 
# a ,b = 3,4
# print(a+b)
# print(a+b)
# print(a*b)
# print(a/b)
# print(a**b) # 제곱연산 3의 4승을 의미함 
# print(a%3) # 나눗셈을 통해 나머지를 반환 
# print(8/5) # 나눗셈 
# print(8//5) # 나눗셈후 몪 반환 

# # 1- 2. 문자열 
# print('"Python is very easy." he says.')  # 따옴표 출력을 위한 방법 
# print('Life is too short\nYou need python') 
# print("wookgi"+"wookgi")  #문자열 연결법 
# print("wookgi"*2)  #문자열의 곱셈
# a = "Life is too short, You need Python"
# print(a[0:4]) # 문자열 인덱스를 대조해 슬라이싱 
# print(a[4:])  # 문자열 인덱스를 대조해 슬라이싱 끝까지 뽑아내기 
# print(a[:9])  # 문자열 나누기 
#  # 문자열 포매팅 
# y= 3.141414124
# print("I eat %d apples." % 3) #문자열안에 정수값을 대입 
# print("I eat %s apples." % "five")  # 문자열을 대입 
# print("I eat {0} apples".format(3))   #포맷 함수를 이용한 대입 
# print("I ate {0} apples. so I was sick for {1} days.".format(3, 4)) ## 두개 넣기 
# print("{0:<10}".format("hi")) # 왼쪽 정렬 
# print("{0:0.4f}".format(y)) # 포맷을 이용한 소수점 출력 

# # 1- 3. 리스트 자료형 
# odd = [1, 3, 5, 7, 9]
# print(odd)
# a = [1, 2, ['a', 'b', ['Life', 'is']]]
# print (a[2][2][0]) # 삼중리스트 출력 
# print(odd[:2]) # 리스트도 인덱스 대조해 끝까지 뽑아내기 가능함 

# # 1- 3. 튜플 자료형 -> 요소값이 변경되지 않음 
# t3 = (1, 2, 3)
# t4 = 1, 2, 3 

# 2. for문을 한 번 써보자 
""" for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ... """

# 3. 파이썬에서 함수사용 
def add (a,b):
    return a+b

print(add(1,4))