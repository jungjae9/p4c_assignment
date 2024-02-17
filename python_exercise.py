import random
from numpy import arange
print(arange(1, 10))
ran_num = random.randint(1, 10)
print(ran_num)
# 정수
a = 20
print(a)
# 실수
b = 1.4
print(b)
# 복소수
c = 1 + 8j
print(c)
# 문자열
name = "park"
#불리언
end = True

while(end):
    end_str = input()
    if(end_str == 'end'):
        end = False
#리스트
#리스트 초기화
name_list = list()
name_list = ["angela", "jjanggu", "damon"]
print(name_list[1]) # "jjanggu"
#튜플
#튜플 초기화
name_tuple = tuple()
name_tuple = ("angela", "jjanggu", "damon")
print(name_tuple[1])
#딕셔너리
#딕셔너리 초기화
name_num = dict()
name_age = {"name" : "angela", "age" : 40}
print(name_age['name']) # "angela"
#집합
#집합 초기화
num_list1 = set()
num_list2 = set()
num_list1 = {3, 5, 66, 44, 6, 20, 19, 390}
num_list2 = {66, 20, 19 , 409, 18, 7, 91, 89, 73}
# 교집합
print(num_list1 & num_list2) #{19, 20, 66}
#차집합
print(num_list1 - num_list2) #{3, 5, 6, 44, 390}
#합집합
print(num_list1 | num_list2) #{3, 5, 6, 7, 18, 19, 20, 44, 66, 73, 89, 91, 390, 409}
# x가 y보다 크면 코드 실행
x = 9
y = 5
if(x > y):
    print("x가 y보다 크다")
elif(x == y):
    print("x와 y가 같다")
else:
    print("x와 y가 같지 않다")

# for문으로 리스트의 모든 요소 출력
for_list = ['사과', '안녕', 1, 19, 1.9, True]
for i in for_list:
    print(i)

#while문으로 1부터 100까지 합 출력
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

#break를 입력시 종료되는 while문
iuput_str = ''
while(True):
    input_str = input()
    if input_str == 'break':
        break
    print('반복중')

# 리스트 요소의 값이 3이면 출력하지 않고 다음 순회로 건너뛰는 코드
num_list =[1, 2, 3, 4, 5,6 , 7, 8, 9]
for num in num_list:
    if num == 3:
        continue
    print(num)

#두 수를 더한 결과 값을 반화해주는 함수
def add(a, b):
    return a+b
result = add(9, 8)
print(result)

#매개변수와 리턴값이 없는 함수
def Hello():
    print('Hello')
Hello()

#튜플 자료형을 이용해 두 개의 값 반환
def two_return(a,b):
    return a+b, a-b
result1, result2 = two_return(98, 29)
print(result1)
print(result2)