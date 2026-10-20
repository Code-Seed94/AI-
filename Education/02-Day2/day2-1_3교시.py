# 3교시 시작
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
for key, value in dict1.items():
    print(key, value) 
# 더 간단하게 key와 value를 가져올 수 있다
# gpt 진행으로 이동 - 딕셔너리 예제와 설명 검색

# 딕셔너리는 순서를 보장하지 않는다 
# 따라서 value과 묶여진 key로 가져온다
# pop이나 del은 고유 키로 삭제한다 
# pop은 삭제한 쌍을 반환하여 볼 수 있다






# 백앤드 - API에서 요청을 보낸 사용자 정보(dict)를 검증해서
# 접근 가능 여부와 부여할 기능을 판별하는 분기 로직을 작성


# 시나리오
# 요구사항
# 1. 사용자 정보는 user_role(문자열)과 is_suspended(정지계정여부)
# 2. is_suspended가 True이면 즉시 "정지된 계정입니다."를 출력 후 검사 종료


# 3. 역할은 admin,manager,user,guest 중 하나

# admin: "전체 시스템 관리 및 데이터 수정 권한 부여"

# manager: "팀 데이터 조회 및 수정 권한 부여"

# user: "개인 데이터 조회 권한 부여"

# guest: "게스트 권한 (읽기 전용 일부 허용)"

# 4. 정의되지 않은 역할일 경우 : [오류] 알 수 없는 계정입니다.


# test_users = 딕셔너리 여러 개를 담은 리스트다
test_users = [
    {"username": "alpha", "user_role": "admin", "is_suspended": False},
    {"username": "bravo", "user_role": "user", "is_suspended": True},
    {"username": "charlie", "user_role": "manager", "is_suspended": False},
    {"username": "delta", "user_role": "hacker", "is_suspended": False},
]

for user in test_users:
    username = user['username']
    role = user['user_role']
    suspended = user['is_suspended']

# 3교시 종료






