#  Codex API 토큰 쿼터 및 프롬프트 보안 제어 시스템

class AIServiceError(Exception):
    """AI 서비스 최상위 기본 예외 클래스"""
    pass


class PromptEmptyError(AIServiceError):
    """프롬프트가 비어있을 때 발생하는 예외"""
    pass


class TokenQuotaExceededError(AIServiceError):
    """토큰 한도 초과 시 요청량과 잔여 한도 컨텍스트를 함께 전달하는 예외"""

    def __init__(self, requested: int, remaining: int):
        self.requested = requested
        self.remaining = remaining
        super().__init__(
            f"토큰 한도 초과! (요청: {requested}개, 잔여 한도: {remaining}개)"
        )


class CodexClient:
    def __init__(self, daily_quota: int = 100):
        self.remaining_tokens = daily_quota

    def generate_code(self, prompt: str, estimated_tokens: int) -> str:
        if not prompt.strip(): # not 프롬프트가 비어있는 경우 실행한다 
            raise PromptEmptyError(
                "프롬프트에 최소 1글자 이상의 명령어를 입력해주세요."
            )

        if estimated_tokens > self.remaining_tokens:
            raise TokenQuotaExceededError(
                estimated_tokens,
                self.remaining_tokens,
            )

        self.remaining_tokens -= estimated_tokens

        return (
            f"[생성 성공] '{prompt}' 코드 생성 완료 "
            f"(남은 토큰: {self.remaining_tokens})"
        )


client = CodexClient(daily_quota=50)

test_requests = [
    ("클래스 리팩토링 코드 작성", 30),
    ("   ", 10),
    ("대규모 프로젝트 전체 변환", 40),
]

for prompt_text, tokens in test_requests:
    try:
        result = client.generate_code(prompt_text, tokens)
        print(result)

    except PromptEmptyError as e:
        print(f"[입력 검증 실패] {e}")

    except TokenQuotaExceededError as e:
        print(
            f"[쿼터 경보] {e} -> "
            "기본 요금제를 업그레이드하거나 요청 길이를 줄이세요."
        )


# 실행 결과:
# [생성 성공] '클래스 리팩토링 코드 작성' 코드 생성 완료 (남은 토큰: 20)
# [입력 검증 실패] 프롬프트에 최소 1글자 이상의 명령어를 입력해주세요.
# [쿼터 경보] 토큰 한도 초과! (요청: 40개, 잔여 한도: 20개) -> 기본 요금제를 업그레이드하거나 요청 길이를 줄이세요.





















# 아래는 주석 해석 포함 코드

# 먼저 프로그램의 전체 흐름을 알아봅시다.
#
#   ① 사용할 수 있는 토큰 수를 정합니다.
#   ② 코드 생성 요청을 받습니다.
#   ③ 요청 내용이 비어 있는지 검사합니다.
#   ④ 남은 토큰이 충분한지 검사합니다.
#   ⑤ 문제가 없으면 토큰을 차감하고 성공 안내문을 반환합니다.
#   ⑥ 문제가 있으면 오류를 발생시키고, 호출한 곳에서 처리합니다.
#
# 여기서는 실제 AI 서비스에 접속하지 않습니다.
# 토큰 수를 관리하고 성공 문자열을 반환하는 연습용 코드입니다.
#
# 토큰(token):
#   AI 모델이 텍스트를 처리하는 단위입니다.
#   글자 수나 단어 수와 항상 일치하지는 않습니다.
#
# 이 예제에서는 토큰 수를 직접 계산하지 않고,
# 요청할 때 전달한 예상 토큰 수를 사용합니다.


# 1. 이 프로그램에서 사용할 예외들의 공통 부모를 만듭니다.
#
# 예외(exception):
#   프로그램 실행 중 발생한 문제를 나타내는 객체입니다.
#
# Exception:
#   파이썬이 기본으로 제공하는 예외 클래스입니다.
#
# class AIServiceError(Exception):
#   Exception을 상속받아 새로운 예외 종류를 만든다는 뜻입니다.
#
# 이렇게 개발자가 직접 만든 예외를 '사용자 정의 예외'라고 합니다.
class AIServiceError(Exception):

    # 함수나 클래스 정의 바로 아래에 적은 문자열을
    # '독스트링(docstring)'이라고 합니다.
    #
    # 이 클래스가 어떤 역할인지 설명하는 문서용 문자열입니다.
    # # 주석과는 문법적으로 다르며, 설명 정보를 조회할 때 사용할 수 있습니다.
    """AI 서비스 최상위 기본 예외 클래스"""

    # pass는 아무 작업도 하지 않는 문법입니다.
    #
    # 여기서는 추가 기능을 작성하지 않고,
    # 부모인 Exception의 기능을 그대로 물려받아 사용합니다.
    pass


# 2. 프롬프트가 비어 있을 때 사용할 예외를 만듭니다.
#
# 프롬프트(prompt):
#   AI에게 전달하는 질문이나 작업 지시문입니다.
#
# PromptEmptyError는 AIServiceError를 상속받습니다.
# 따라서 이 예외도 AI 서비스 오류의 한 종류가 됩니다.
class PromptEmptyError(AIServiceError):
    """프롬프트가 비어있을 때 발생하는 예외"""

    # 별도의 처리 기능 없이
    # '입력 내용이 비어 있음'을 구분하는 예외 이름으로 사용합니다.
    #
    # 초기화 메서드를 직접 작성하지 않았으므로,
    # 부모에게서 물려받은 초기화 기능으로 오류 메시지를 받을 수 있습니다.
    pass


# 3. 토큰 한도를 초과했을 때 사용할 예외를 만듭니다.
#
# TokenQuotaExceededError라는 이름은 다음 의미로 지었습니다.
#
#   Token    → 토큰
#   Quota    → 사용 한도
#   Exceeded → 초과함
#   Error    → 오류
#
# 이 예외도 AIServiceError를 상속받습니다.
class TokenQuotaExceededError(AIServiceError):
    """토큰 한도 초과 시 요청량과 잔여 한도 컨텍스트를 함께 전달하는 예외"""

    # 이 예외는 오류 문구뿐 아니라
    # 요청한 토큰 수와 남은 토큰 수도 함께 저장합니다.
    #
    # __init__:
    #   예외 객체를 만들 때 실행되는 초기화 메서드입니다.
    #
    # self:
    #   지금 만드는 예외 객체 자신입니다.
    #
    # requested: int:
    #   요청에 필요한 토큰 수를 정수로 전달받습니다.
    #
    # remaining: int:
    #   현재 남은 토큰 수를 정수로 전달받습니다.
    #
    # : int는 타입 힌트입니다.
    # 정수를 기대한다는 뜻이며, 입력값을 자동으로 검사하지는 않습니다.
    def __init__(self, requested: int, remaining: int):

        # 요청한 토큰 수를 이 예외 객체에 저장합니다.
        self.requested = requested

        # 남아 있던 토큰 수도 예외 객체에 저장합니다.
        #
        # 나중에 이 예외를 e라는 이름으로 받으면
        # e.requested와 e.remaining으로 각각 조회할 수 있습니다.
        self.remaining = remaining

        # 부모에게서 물려받은 예외 초기화 기능을 실행합니다.
        #
        # super()는 부모 쪽 기능을 사용할 때 쓰는 문법입니다.
        # 여기서는 상속 관계를 따라 Exception의 초기화 기능을 사용합니다.
        #
        # 완성된 오류 메시지를 전달하여
        # 예외 객체를 문자열로 표시할 때 이 문구가 나오도록 합니다.
        #
        # f"..."는 문자열 안에 실제 값을 넣는 문법입니다.
        # {requested}, {remaining} 자리에 전달받은 숫자가 들어갑니다.
        super().__init__(
            f"토큰 한도 초과! (요청: {requested}개, 잔여 한도: {remaining}개)"
        )


# 지금까지 만든 예외들의 상속 관계:
#
# Exception
#   └─ AIServiceError
#       ├─ PromptEmptyError
#       └─ TokenQuotaExceededError
#
# 이렇게 공통 부모를 두면
# 세부 오류를 각각 처리하거나,
# AIServiceError라는 공통 종류로 묶어서 처리할 수 있습니다.
#
# 아래 실행 코드에서는 두 세부 오류를 각각 처리합니다.


# 4. 코드 생성 요청과 토큰 잔량을 관리하는 클래스를 만듭니다.
#
# CodexClient는 이 예제에서 직접 지은 클래스 이름입니다.
# 이 클래스가 객체별로 남은 토큰 수를 기억합니다.
class CodexClient:

    # 객체를 처음 만들 때 사용할 초기화 메서드입니다.
    #
    # daily_quota: int = 100:
    #   처음 사용할 수 있는 토큰 수를 전달받습니다.
    #   값을 생략하면 기본값 100을 사용합니다.
    #
    # 예:
    #   CodexClient()               → 처음 토큰 100개
    #   CodexClient(daily_quota=50) → 처음 토큰 50개
    def __init__(self, daily_quota: int = 100):

        # 전달받은 한도를 현재 남은 토큰 수로 저장합니다.
        #
        # remaining_tokens는 '남은 토큰들'이라는 뜻으로 지은 속성 이름입니다.
        #
        # daily_quota라는 이름을 사용했지만,
        # 날짜에 맞춰 한도를 자동으로 초기화하는 기능은 이 코드에 없습니다.
        self.remaining_tokens = daily_quota

    # 5. 코드 생성 요청을 처리하는 메서드입니다.
    #
    # prompt: str:
    #   사용자의 작업 지시문을 문자열로 전달받습니다.
    #
    # estimated_tokens: int:
    #   이 요청에 사용할 것으로 예상하는 토큰 수를 전달받습니다.
    #
    # -> str:
    #   정상 처리되면 문자열을 반환한다는 타입 힌트입니다.
    def generate_code(self, prompt: str, estimated_tokens: int) -> str:

        # 6. 프롬프트가 비어 있는지 검사합니다.
        #
        # prompt.strip():
        #   문자열 양쪽 끝의 공백이나 줄바꿈 등을 제거한 문자열을 만듭니다.
        #
        # 예:
        #   "  안녕하세요  ".strip() → "안녕하세요"
        #   "   ".strip()          → ""
        #
        # strip()은 원래 prompt 자체를 변경하지 않습니다.
        #
        # 빈 문자열 ""은 조건식에서 거짓으로 취급됩니다.
        # not은 참과 거짓을 뒤집습니다.
        #
        # 따라서 이 조건은
        # '앞뒤 공백을 제거했더니 아무 내용도 없다면'이라는 뜻입니다.
        if not prompt.strip():

            # raise는 예외를 발생시키는 문법입니다.
            #
            # PromptEmptyError(...)로 예외 객체를 만들고,
            # raise로 그 예외가 발생했음을 알립니다.
            #
            # 예외가 발생하면 이 메서드의 아래 코드를 계속 실행하지 않고
            # 호출한 곳의 예외 처리 코드로 이동합니다.
            #
            # 따라서 토큰 검사나 토큰 차감도 실행되지 않습니다.
            raise PromptEmptyError(
                "프롬프트에 최소 1글자 이상의 명령어를 입력해주세요."
            )

        # 7. 필요한 토큰이 현재 잔량보다 많은지 검사합니다.
        #
        # >는 왼쪽 값이 오른쪽 값보다 큰지 비교합니다.
        #
        # 예:
        #   필요한 토큰 40개 > 남은 토큰 20개 → 참
        #   필요한 토큰 20개 > 남은 토큰 20개 → 거짓
        #
        # 필요한 양과 남은 양이 같으면 이 검사는 통과합니다.
        if estimated_tokens > self.remaining_tokens:

            # 토큰 한도 초과 예외를 만들어 발생시킵니다.
            #
            # estimated_tokens는 예외의 requested로,
            # self.remaining_tokens는 예외의 remaining으로 전달됩니다.
            #
            # 예외 객체의 __init__이 두 숫자를 저장하고
            # 오류 메시지를 구성합니다.
            #
            # 이 경우에도 아래의 토큰 차감 코드는 실행되지 않습니다.
            raise TokenQuotaExceededError(
                estimated_tokens,
                self.remaining_tokens
            )

        # 8. 두 검사를 통과했으므로 토큰을 차감합니다.
        #
        # -=는 기존 값에서 오른쪽 값을 빼서 다시 저장하는 문법입니다.
        #
        # 다음 코드와 같은 뜻입니다.
        # self.remaining_tokens = self.remaining_tokens - estimated_tokens
        #
        # 예: 50개에서 30개를 사용하면 20개가 남습니다.
        self.remaining_tokens -= estimated_tokens

        # 9. 성공 안내문을 반환합니다.
        #
        # {prompt}에는 전달받은 원래 지시문이 들어갑니다.
        # {self.remaining_tokens}에는 차감 후 잔량이 들어갑니다.
        #
        # return은 결과를 호출한 곳에 돌려줍니다.
        # 이 줄 자체가 화면에 출력하는 것은 아닙니다.
        return f"[생성 성공] '{prompt}' 코드 생성 완료 (남은 토큰: {self.remaining_tokens})"


# 10. 처음에 토큰 50개를 가진 객체를 만듭니다.
#
# daily_quota=50처럼 매개변수 이름을 적어 전달하는 방식을
# '키워드 인자'라고 합니다.
#
# 기본값은 100이지만, 여기서는 50을 명시했으므로 50을 사용합니다.
#
# 만들어진 객체를 client라는 변수로 가리키게 합니다.
client = CodexClient(daily_quota=50)


# 11. 시험할 요청들을 리스트에 담습니다.
#
# 바깥쪽 대괄호 []는 리스트입니다.
# 안쪽의 ("문자열", 숫자)는 두 값을 묶은 튜플입니다.
#
# 각 튜플에는 다음 정보가 들어 있습니다.
#
#   첫 번째 값 → 작업 지시문
#   두 번째 값 → 예상 토큰 사용량
test_requests = [

    # 정상 요청입니다.
    # 처음 잔량 50개에서 30개를 사용하므로 20개가 남습니다.
    ("클래스 리팩토링 코드 작성", 30),

    # 공백만 들어 있는 요청입니다.
    # strip()을 적용하면 빈 문자열이 되어 입력 오류가 발생합니다.
    ("   ", 10),

    # 내용은 있지만 토큰이 부족한 요청입니다.
    # 필요한 양은 40개인데, 앞선 정상 요청 후 잔량은 20개입니다.
    ("대규모 프로젝트 전체 변환", 40),
]


# 12. 요청을 하나씩 꺼내 처리합니다.
#
# 각 튜플의 두 값을 각각 다른 이름으로 받습니다.
# 이렇게 묶인 값을 나누어 받는 것을 '언패킹'이라고 합니다.
#
# prompt_text → 작업 지시문
# tokens      → 예상 토큰 사용량
#
# 첫 번째 반복에서는:
#   prompt_text = "클래스 리팩토링 코드 작성"
#   tokens = 30
for prompt_text, tokens in test_requests:

    # 13. 예외가 발생할 수 있는 작업을 try 안에서 실행합니다.
    #
    # try가 반복문 안에 있으므로
    # 각 요청마다 별도로 예외를 처리할 수 있습니다.
    try:

        # 현재 요청을 코드 생성 메서드에 전달합니다.
        #
        # prompt_text → generate_code의 prompt
        # tokens      → generate_code의 estimated_tokens
        #
        # 정상 처리되면 반환된 성공 문자열을 result에 저장합니다.
        #
        # 예외가 발생하면 대입이 완료되지 않고
        # 해당 except로 이동합니다.
        result = client.generate_code(prompt_text, tokens)

        # 정상 처리된 경우에만 이 줄까지 도달합니다.
        # 반환받은 성공 안내문을 화면에 출력합니다.
        print(result)

    # 14. 입력 내용이 비어 있는 예외를 처리합니다.
    #
    # PromptEmptyError가 발생했을 때 이 블록이 실행됩니다.
    #
    # as e는 발생한 예외 객체를 e라는 이름으로 사용한다는 뜻입니다.
    except PromptEmptyError as e:

        # {e}를 문자열 안에 넣으면
        # 예외 객체가 가지고 있는 오류 메시지가 표시됩니다.
        print(f"[입력 검증 실패] {e}")

    # 15. 토큰 한도를 초과한 예외를 처리합니다.
    #
    # TokenQuotaExceededError가 발생했을 때 이 블록이 실행됩니다.
    except TokenQuotaExceededError as e:

        # 예외의 오류 메시지 뒤에 대응 방법 안내를 붙여 출력합니다.
        #
        # 업그레이드는 안내 문구입니다.
        # 실제 요금제를 변경하는 작업이 실행되는 것은 아닙니다.
        print(f"[쿼터 경보] {e} -> 기본 요금제를 업그레이드하거나 요청 길이를 줄이세요.")

    # 해당 요청의 처리나 예외 처리가 끝나면
    # for문이 다음 요청을 꺼냅니다.
    #
    # client는 반복문 바깥에서 한 번 만들었으므로
    # 남은 토큰 수는 다음 요청에도 이어서 유지됩니다.


# 실제 화면에 출력되는 세 줄:
#
# [생성 성공] '클래스 리팩토링 코드 작성' 코드 생성 완료 (남은 토큰: 20)
# [입력 검증 실패] 프롬프트에 최소 1글자 이상의 명령어를 입력해주세요.
# [쿼터 경보] 토큰 한도 초과! (요청: 40개, 잔여 한도: 20개) -> 기본 요금제를 업그레이드하거나 요청 길이를 줄이세요.
#
#
# 토큰 잔량 변화를 따라가 봅시다.
#
# 시작:
#   50개
#
# 첫 번째 요청:
#   검사 통과 → 30개 차감 → 20개
#
# 두 번째 요청:
#   공백 입력 감지 → 예외 발생 → 차감 없이 20개 유지
#
# 세 번째 요청:
#   토큰 부족 감지 → 예외 발생 → 차감 없이 20개 유지
#
#
# 마지막으로 세 문법의 차이를 구분해 봅시다.
#
# return:
#   정상 결과를 호출한 곳에 돌려주고 함수를 끝냅니다.
#
# raise:
#   예외를 발생시키고, 그 예외를 처리할 곳으로 실행 흐름을 넘깁니다.
#
# except:
#   지정한 종류의 예외를 받아 어떻게 대응할지 실행합니다.