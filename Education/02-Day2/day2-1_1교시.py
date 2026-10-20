# if - elif - else
score = int(input('점수'))
if score >=90:
    print('A')
elif score >=80:
    print('B')
elif score >=70:
    print('C')
else:
    print('F')






# 논리 연산자 is Python에서 is는 두 변수가 
# 같은 객체를 가리키는지 비교하는 연산자

# and는 곱하기 = t + t 인 경우를 제외하고 모두 False
# t = 1 , f = 0 /ane는 곱하기로 이해
# 즉 isSuccess = 0 , isPass = 1 
# 프로그래밍에서는 0을 제외한 모든 수는 True로 간주
# and = 0을 만나는 순간 즉시 종료

# or는 더하기 = t + t , t + f , f + t 인 경우 모두 True
# 즉 True가 하나만 있어도 True로 간주
# 왜? 더하여 합해지는 거니까

isSuccess = True
isPass = False

if isSuccess and isPass:
    print('A')
else:
    print('B')






#단락평가 short-circuit #evaluation
if isSuccess and isPass and isSuccess:
    print('통과')
if isSuccess or isPass or isSuccess:
    print('통과')


def expensive_check():
    print('시간이 오래 걸리는 함수 실행')   
    return True

is_active = False
if is_active and expensive_check(): #and는 차단(expensive_check 함수 실행 안됨)
if is_active or expensive_check(): #or은 통과
    print('통과')
else:
    print('차단 (expensive_check 함수 실행 안됨)')

# None 값을 방어

user_profile = None

# is not None and 에서는 넌이 아니면 True로 간주

if user_profile is not None and user_profile.get('is_verified'):
    print('인증된 사용자')
else:
    print('비인증 사용자')

# 1교시 종료






