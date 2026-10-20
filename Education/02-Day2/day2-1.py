# # if - elif - else
# score = int(input('점수'))
# if score >=90:
#     print('A')
# elif score >=80:
#     print('B')
# elif score >=70:
#     print('C')
# else:
#     print('F')






# # 논리 연산자 is Python에서 is는 두 변수가 
# # 같은 객체를 가리키는지 비교하는 연산자

# # and는 곱하기 = t + t 인 경우를 제외하고 모두 False
# # t = 1 , f = 0 /ane는 곱하기로 이해
# # 즉 isSuccess = 0 , isPass = 1 
# # 프로그래밍에서는 0을 제외한 모든 수는 True로 간주
# # and = 0을 만나는 순간 즉시 종료

# # or는 더하기 = t + t , t + f , f + t 인 경우 모두 True
# # 즉 True가 하나만 있어도 True로 간주
# # 왜? 더하여 합해지는 거니까

# isSuccess = True
# isPass = False

# if isSuccess and isPass:
#     print('A')
# else:
#     print('B')






# #단락평가 short-circuit #evaluation
# if isSuccess and isPass and isSuccess:
#     print('통과')
# if isSuccess or isPass or isSuccess:
#     print('통과')


# def expensive_check():
#     print('시간이 오래 걸리는 함수 실행')   
#     return True

# is_active = False
# if is_active and expensive_check(): #and는 차단(expensive_check 함수 실행 안됨)
# if is_active or expensive_check(): #or은 통과
#     print('통과')
# else:
#     print('차단 (expensive_check 함수 실행 안됨)')

# None 값을 방어

# user_profile = None

# is not None and 에서는 넌이 아니면 True로 간주

# if user_profile is not None and user_profile.get('is_verified'):
#     print('인증된 사용자')
# else:
#     print('비인증 사용자')

# 1교시 종료






# # 2교시 시작 
# #클래스는 아직 시작하지 않았고 예시로 사용
# class safeprofile:
#     def __init__(self):
#         pass
#     def get(self, key):
#         return 'True'
#     # def set(self, key, value):
#     #     return 'True'

# user_profile = safeprofile() #인증된 사용자
# # user_profile = None #비인증 사용자

# # user_profile2 = safeprofile() #인증된 사용자
# # user_profile3 = safeprofile() #인증된 사용자
# # 위와 같이 여러개를 만들 수 있다

# # user_profile.get('is_verified') # None이 아니므로 True로 간주
# if user_profile :
#     print('인증된 사용자')
# else:
#     print('비인증 사용자')





# # 삼항연산자
# user_score = 85
# if user_score >= 80:
#     grade = 'pass'
# else:
#     grade = 'fail' 
# ## 삼항연산자
# grade = 'pass' if user_score >= 80 else 'fail'
# 삼항연산자 코드를 ##삼항연산자로 작성할 수 있다
# 만약 어떤 조건이 80점 이상이면 grade는 'pass'이고, 
# 그렇지 않으면 'fail'로 설정된다.
#삼항연산자란 if else 문을 한 줄로 표현하는 방법이다.





#포함관계(in, not in)
# role = 'admin'

# if role == 'admin' or role == 'manager' or role == 'staff'

# allowed_roles = ['admin', 'manager', 'staff']
# if role in allowed_roles:
#     print('권한 있음')
# else:
#     print('권한 없음')
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

# list1 = [10, 20, 30, 40,[1, 2, 3, 4]]

# dict1 = {'kor':80, 'eng': 80, 'math': 90, 'science': 70}
# # 이름은 동명이인이지만 각자의 주민번호는 다르다
# # 홍길동 이라는 단어는 하나, 하지만 그 안에 여러 개의 값이 들어있다
# # 이름, 주민번호, 주소, 전화번호, 이메일 등등

# dict1.keys() # key만 가져오기
# dict1.values() # value만 가져오기
# dict1.items() # key, value 쌍으로 가져오기

# for i in dict1.keys(): # key만 가져오기
# for i in dict1. values(): # value만 가져오기
# for i in dict1.items(): # key, value 쌍으로 가져오기

    # print(i) # key만 가져오기 전체 값
    # print(i[0],i[1]) # key(0)와 value(1) 함께 가져오기

# 2교시 종료







# 3교시 시작

# for key, value in dict1.items():
#     print(key, value) 
# 더 간단하게 key와 value를 가져올 수 있다
#gpt 진행으로 이동 - 딕셔너리 예제와 설명 검색

#딕셔너리는 순서를 보장하지 않는다 
# 따라서 value과 묶여진 key로 가져온다
#pop이나 del은 고유 키로 삭제한다 
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
# test_users = [
#     {"username": "alpha", "user_role": "admin", "is_suspended": False},
#     {"username": "bravo", "user_role": "user", "is_suspended": True},
#     {"username": "charlie", "user_role": "manager", "is_suspended": False},
#     {"username": "delta", "user_role": "hacker", "is_suspended": False},
# ]

# for user in test_users:
#     username = user['username']
#     role = user['user_role']
#     suspended = user['is_suspended']

# 3교시 종료






# 4교시 시작 
# gpt로 이후 코드 작성 요청했음 

# test_users는 딕셔너리 여러 개를 담은 "리스트"
# "리스트" 에서 딕셔너리를 하나씩 꺼내 user에 넣습니다.

# for user in test_users: # test_users의 key, value를 user로 할당
#     username = user["username"] # user는 딕셔너리 타입이 되었고, 그 중 key인 ["username"]을 username이라는 변수에 할당
#     role = user["user_role"] # user는 딕셔너리 타입이 되었고, 그 중 key인 ["user_role"]을 role이라는 변수에 할당
#     suspended = user["is_suspended"] # user는 딕셔너리 타입이 되었고, 그 중 key인 ["is_suspended"]을 suspended라는 변수에 할당

# # 즉, user에 할당된 각 쌍으로 된 딕셔너리 deta에서 해당하는 각 key ["username"],["user_role"], ["is_suspended"]를 
# # username, role, suspended라는 변수에 할당

#     if suspended: # suspended가 True인지 확인
#         print(f"{username}: 정지된 계정입니다.") # username 변수와 정지 안내 메시지를 한 줄로 출력
#         continue # 현재 사용자 검사를 종료하고 다음 user의 반복으로 이동

#     message = role_messages.get( # role_messages 딕셔너리에서 역할에 해당하는 메시지를 가져와 message 변수에 할당
#         role, # role 변수의 값을 role_messages에서 찾을 key로 사용
#         "[오류] 알 수 없는 계정입니다." # role에 해당하는 key가 없을 경우 사용할 기본 메시지
#     ) # get 메서드 호출을 종료

#     print(f"{username}: {message}")  # username과 역할에 맞는 message를 한 줄로 출력


# suspended가 True이면 정지된 계정이라는 메시지를 출력하고 다음 사용자로 넘어감
# suspended가 False이면 role_messages에서 role에 맞는 권한 메시지를 찾음
# role이 role_messages에 없으면 "[오류] 알 수 없는 계정입니다."를 message에 할당
# 마지막으로 username과 message를 한 줄로 출력



#브레이크 반대 컨티뉴 
# 컨티뉴 있는 문장은 무시하고 일단 진행
# continus
# continus의 예제
# list_a = [1,2,3,4,5,6,7,8,9,10]

# for i in list_a:   # list_a의 값을 하나씩 꺼내 i 변수에 할당하며 순환
#     if i % 2 == 0: # i % 2 == 0은 i를 2로 나눈 나머지가 0이므로 짝수인지 확인하는 조건 
    
    #if i % 2 != 0:# i를 2로 나눈 나머지가 0이 아닐때 즉, 홀 수 일때 Ture

                   # 짝수이면 아래 print(i)를 실행하지 않고 다음 숫자로 이동

    # if i == 5:   # 순환을 계속 5만 제외하고 출력 

    #     continue   # 조건이 해당하면 현재 회차의 print(i)를 건너뛰고 다음 숫자로 이동 즉, 처음으로 돌아가서 재시작
    # print(i)       # continue에 해당하지 않은 조건의 수만 출력

# continue는 값이 맞는 것을 확인 혹은 아닌 것을 확인해라 라는 조건일 때 
# 아래에 오게되면 그 조건에 해당하면 처음으로 돌아가는 것 즉, 그 아래 줄은 계산하지 않는 것이다


# 4교시 종료





# 점심 시간





# 5교시 시작

# 바이브 코딩이란?
# What : 무엇을 만들지
# consistants : 어떤 제약으로 동작해야 하는지
# How : 어떻게 구현하는지
# Vibe Check : 결과를 검증

# 3대 핵심 룰 P(Prompt) -> G(Generater) -> V(Validater)
# P = 입력(input), cnffur(output), 알고리즘 제약 조건, 함수 명시
# V = 결과 검증, 테스트 케이스 검증

# ex) 1부터 100까지 합 구하기
# bad : 짝수 합 구해줘
# good:

# [problem] 1qnxj 까지의 정수 중 짝수들의 합과 짝수의 총 개수를 계산한다
# [Function] calculate_even_sum_and_count(n)
# [Rules]
#     - n이 1 미만인 경우 합 0, 개수 0을 반환할것
#     - for 문과 if 문을 활용하여 짝수(i % 2 ==0)를 판단할 것
# [Output]    {"Sum": int, "Count":int  }
# gpt로 작성





# # 실습 규칙
# '''문제 정의 / 입력값 / 출력 값 / 제약 조건을 작성
# assert 함수를 활용하여 테스트 케이스'''

# [Mission 1: Smart FizzBuzz Analyzer]
# - 함수명: analyze_fizzbuzz(limit: int) -> dict
# - 로직 제약:
#   1. 1부터 limit까지 순회한다.
#   2. 3의 배수이면서 5의 배수이면: "FizzBuzz" 카운트 증가
#   3. 3의 배수이면: "Fizz" 카운트 증가
#   4. 5의 배수이면: "Buzz" 카운트 증가
#   5. 그 외의 숫자이면: "Number" 카운트 증가
# - 반환값 형식:
#   {"FizzBuzz": int, "Fizz": int, "Buzz": int, "Number": int}
# - 엣지 케이스: limit가 1 미만인 경우 모든 카운트가 0인 딕셔너리 반환
#  gpt로 소스파일 제작 완료




# # zip
# list_1 = ['a','b','c']
# list_2 = [100,200,300]
# result = zip(list_1,list_2)
# # print(range(5))



# # 5교시 종료







# # 6교시 시작

# # for i in result:
# #     print(i) # zip 형태로 한번 반환했기 때문에 384줄의 print를 해도 값이 없다로 나온다 다시 돌려서 임시 값을 만들고 변환해야 반환된다.

# ## 첫번째 두번째 세번째 끼리끼리 묶는다 zip
# ## zip은 출력(반환) 후 사라짐 한번 소비하면 다시 사용할 수 없는 이터레이터 (임시 데이터)

# # zip으로 생성한 객체를 dictionary로 변환
# result = dict(result)
# print(result)








# # R I O C 
# # Role : 역할
# # input : 입력
# # output : 출력
# # constraints : 제약 조건(어떤 알고리즘/규칙, 뭘 하지 말아야 하는지)


# 프롬프트 예시


# [Role]
# 너는 온라인 게임 채팅 시스템의 백엔드 파이썬 개발자야.

# [Task]
# 채팅 메시지에서 금지 단어를 찾아 마스킹(*) 처리하는 함수를 작성해줘.

# [Input]
# 1. chat_message (str): 사용자가 입력한 채팅 메시지
# 2. bad_words (list[str]): 금지 단어 목록

# [Output]
# - masked_message (str): 금지어가 '*'로 치환된 최종 문자열

# [Constraints & Logic]
# - 함수명: mask_bad_words(chat_message: str, bad_words: list[str]) -> str
# - 금지 단어의 글자 수만큼 '*'로 치환할 것 (예: "바보" -> "**")
# - 대소문자를 구분하지 않고 찾되, 원본 메시지의 다른 문장 구조는 그대로 보존할 것
# - 주석으로 각 핵심 라인이 어떻게 동작하는지 초보자도 알기 쉽게 달아줄 것
# - 생성하는 코드는 대중적으로 해석하기 쉬운 기분 문법과 라이브러리 만을 사용할것
# - 생성된 코드는 오류가 없는지 확인할 것 예측 가능한 테스트케이스를 (assert 사용) 다양하게 만들고 실행해서 오류가 있으면 수정할 것

# 아래는 내가 작성한 gpt 명령문이다

# 위 내용 중 [Constraints & Logic] 아래 내용의 명령을 가장 완성도 있는 답변을 받을 수 있는 질문으로 설계하고 
# 마크다운 코드로 작성해 [Constraints & Logic]아래의 내용만 해당되 [Constraints & Logic] 위에 내용은 그대로 작성해



# 설계된 질문


# [Role]
# 너는 온라인 게임 채팅 시스템의 백엔드 파이썬 개발자야.

# [Task]
# 채팅 메시지에서 금지 단어를 찾아 마스킹(*) 처리하는 함수를 작성해줘.

# [Input]
# 1. chat_message (str): 사용자가 입력한 채팅 메시지
# 2. bad_words (list[str]): 금지 단어 목록

# [Output]
# - masked_message (str): 금지어가 '*'로 치환된 최종 문자열

# [Constraints & Logic]

# 다음 요구사항에 맞춰 함수를 구현하고, assert 테스트로 정확성을 검증해줘.

# 1. 함수 정의
#    - 함수명과 타입 힌트는 아래 형태를 정확히 사용할 것.
#      def mask_bad_words(chat_message: str, bad_words: list[str]) -> str:
#    - 입력은 명시된 타입으로 전달된다고 가정하며, 불필요한 타입 검사나 예외 처리는 추가하지 말 것.
#    - 입력받은 bad_words 목록을 변경하지 말 것.

# 2. 금지어 탐지 및 마스킹 규칙
#    - 영문 대소문자를 구분하지 않고 금지어를 찾을 것.
#    - 단어 경계와 관계없이 메시지에 포함된 모든 금지어를 찾을 것.
#      예: "왕바보야"에서 "바보"를 마스킹하면 "왕**야".
#    - 일치한 원본 메시지의 각 문자를 '*' 한 개로 치환할 것.
#      예: "바보" → "**", "BAD" → "***".
#    - 동일한 금지어가 여러 번 등장하면 모든 위치를 마스킹할 것.
#    - 금지어가 서로 겹치거나 다른 금지어를 포함하면, 일치하는 모든 영역을 합쳐 마스킹할 것.
#      예: 메시지 "abcde", 금지어 ["abc", "cde"] → "*****".
#    - 모든 일치 위치는 원본 메시지를 기준으로 판단할 것. 먼저 마스킹한 결과 때문에 다른 금지어 탐지가 누락되면 안 됨.
#    - 금지어 목록의 순서나 중복 여부가 결과에 영향을 주지 않도록 할 것.
#    - 금지어는 정규표현식이 아닌 일반 문자열로 취급할 것.
#      예: ".", "*", "c++", "[금지]"에 포함된 기호도 문자 그대로 찾을 것.
#    - 마스킹 대상 이외의 문자는 대소문자, 공백, 줄바꿈, 문장부호를 포함하여 그대로 보존할 것.
#    - 반환 문자열의 길이는 원본 메시지의 길이와 같아야 함.
#    - 글자 수와 위치는 Python 문자열의 len()과 인덱스를 기준으로 할 것.

# 3. 빈 값 처리
#    - chat_message가 빈 문자열이면 빈 문자열을 반환할 것.
#    - bad_words가 빈 목록이면 원본 메시지를 그대로 반환할 것.
#    - bad_words 안의 빈 문자열("")은 무시할 것.
#    - 금지어에 포함된 공백을 임의로 제거하거나 문자열을 수정하지 말 것.

# 4. 코드 작성 기준
#    - Python 3.9 이상에서 실행할 수 있는 기본 문법과 표준 라이브러리만 사용할 것.
#    - 외부 패키지 없이, 유지보수와 가독성을 우선하여 작성할 것.
#    - 의미가 명확한 변수명을 사용하고, 불필요한 클래스나 복잡한 추상화는 피할 것.
#    - 핵심 처리 과정에는 초보자도 이해할 수 있는 한국어 주석을 달 것.
#    - 특히 금지어 탐지, 겹치는 영역 처리, 최종 문자열 생성 과정이 어떻게 동작하는지 설명할 것.

# 5. 테스트 및 검증
#    - 기대 결과를 명시한 assert 테스트를 최소 12개 작성할 것.
#    - 다음 경우를 빠짐없이 포함할 것.
#      - 기본적인 한글 금지어
#      - 영문 대소문자가 섞인 금지어
#      - 동일한 금지어의 반복 및 연속 등장
#      - 여러 종류의 금지어
#      - 단어 내부에 포함된 금지어
#      - 금지어가 없는 메시지
#      - 빈 메시지
#      - 빈 금지어 목록
#      - 빈 문자열이 포함된 금지어 목록
#      - 중복된 금지어
#      - 서로 겹치거나 포함 관계인 금지어
#      - 정규표현식 특수문자가 포함된 금지어
#      - 공백, 줄바꿈, 문장부호의 보존
#    - 금지어 목록의 순서를 바꿔도 결과가 같은지 검증할 것.
#    - 출력 문자열의 길이가 원본과 같은지, 입력 목록이 변경되지 않았는지도 검증할 것.
#    - 테스트를 실제로 실행하고, 실패하면 코드를 수정한 뒤 전체 테스트를 다시 실행할 것.
#    - 실행 환경이 없다면 실행하지 못했다는 사실을 명시하고, 실행했다고 표현하지 말 것.

# [답변 형식]
# 1. 동작 원리를 짧게 설명할 것.
# 2. 함수와 assert 테스트를 포함한, 그대로 복사하여 실행할 수 있는 Python 코드를 제공할 것.
# 3. 실제 테스트 실행 여부와 결과를 간단히 보고할 것.

# 6교시 종료






# 7교시 시작

# # 리스트 컴프리핸션 : 반복과 조건을 이용해 새로운 리스트를 한 줄로 간단히 만드는 문법
# list_1 = [1,2,3,4,5]
# # for i in list_1:
# #     if i %2 == 0:
#       # result.append(i)
# result = [i for i in list_1 if i % 2 == 0] # 위에 3줄을 한줄로 축약

# print(result)


# ages = [20,15,60,25,30,45,5]
# print( [ i for i in ages if i >=20 ])
# print(['성인' if i >=20 else '미성년' for i in ages])

# # 빈 문자열은 거짓 나머지는 트루
# # set()

# num = (1,2,3,4,5,6,7,8,1,2,3,4,5)
# print(set(num))


# # 람다는 이름 없는 함수, def 없이 사용 가능하다

# # gpt로 만든 코드를 해석하는 시간을 가졌다

# 7교시 종료


# # 8교시 시작
# # 디버깅 : 기준 줄을 선택 후  실행 버튼 옆 아래 화살표 클릭 -> 
# # Python Debugger: Debug Python File 클릭 후 노란색 시작 줄 나오면 f11로 한줄 씩 실행하여 결과 확인
# # 실제로 어떻게 진행되는 지 직적 확인하며 이해할 수 있음

# import random
# ages = random.sample(range(10,50),10)
# results = []
# for i in ages:
#     if i>= 20:
#         results.append('성인')
#     else:
#         results.append('미성년자')

# print(results)

# 리스에서 불량을 모두 지우고 정상만 남도록 하기
items = ['정상','불량','불량','정상']
for item in items[:]:
      if item == '불량':
          items.remove('불량')

print(f'검수 결과 : {items}')