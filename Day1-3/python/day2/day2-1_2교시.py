# 2교시 시작 
#클래스는 아직 시작하지 않았고 예시로 사용
class safeprofile:
    def __init__(self):
        pass
    def get(self, key):
        return 'True'
    def set(self, key, value):
        return 'True'

user_profile = safeprofile() #인증된 사용자
# user_profile = None #비인증 사용자

# user_profile2 = safeprofile() #인증된 사용자
# user_profile3 = safeprofile() #인증된 사용자
# 위와 같이 여러개를 만들 수 있다

user_profile.get('is_verified') # None이 아니므로 True로 간주
if user_profile :
    print('인증된 사용자')
else:
    print('비인증 사용자')





 # 삼항연산자
user_score = 85

# if user_score >= 80: #이 4줄은 일반적인 표현
#     grade = 'pass'   #
# else:                # 
#     grade = 'fail'   #
# 
#  
## 삼항연산자란 if else 문을 한 줄로 표현하는 방법이다. 아래 문장이 삼항연산자이다
grade = 'pass' if user_score >= 80 else 'fail'


# 만약 어떤 조건이 80점 이상이면 grade는 'pass'이고, 
# 그렇지 않으면 'fail'로 설정된다.






#포함관계(in, not in)
role = 'admin'

if role == 'admin' or role == 'manager' or role == 'staff':
    allowed_roles = ['admin', 'manager', 'staff']
if role in allowed_roles:
    print('권한 있음')
else:
    print('권한 없음')
# 리스트 중에 하나만 포함되어 있는지 확인
# role은 'admin'이고, allowed_roles 리스트에는 'admin', 'manager', 'staff'가 포함되어 있으므로,
# if role in allowed_roles: 조건이 참(True)으로 평가되어 '권한 있음'을 출력한다.










#딕셔너리
# key : value
# key는 중복될 수 없고, value는 중복될 수 있다
# 한쌍이 하나의 값


#리스트 vs 딕셔너리

# 리스트는 순서가 있고, 인덱스로 접근 가능

# 딕셔너리는 key를 사용하여 value에 접근 가능
# 딕셔너리는 순서가 없어서 인덱스 할 수 없음
# 변수[0],변수[1] 이렇게 key와 value 값만 순서가 있음

list1 = [10, 20, 30, 40,[1, 2, 3, 4]]

dict1 = {'kor':80, 'eng': 80, 'math': 90, 'science': 70}
# 이름은 동명이인이지만 각자의 주민번호는 다르다
# 홍길동 이라는 단어는 하나, 하지만 그 안에 여러 개의 값이 들어있다
# 이름, 주민번호, 주소, 전화번호, 이메일 등등

# dict1.keys() # key만 가져오기
# dict1.values() # value만 가져오기
# dict1.items() # key, value 쌍으로 가져오기

for i in dict1.keys(): # key만 가져오기
# for i in dict1. values(): # value만 가져오기
# for i in dict1.items(): # key, value 쌍으로 가져오기

    print(i) # key만 가져오기 전체 값
    # print(i[0],i[1]) # key(0)와 value(1) 함께 가져오기

# 2교시 종료







