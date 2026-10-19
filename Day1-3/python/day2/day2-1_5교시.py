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
# gpt에서 코드 작성을 요구하였음





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
#  gpt로 소스파일 제작 




# zip
list_1 = ['a','b','c']
list_2 = [100,200,300]
result = zip(list_1,list_2)
print(range(5))



# # 5교시 종료







