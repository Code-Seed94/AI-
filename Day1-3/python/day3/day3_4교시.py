# 멀티모달 AI 모델 통합 추론 파이프라인

class BaseAIModel:
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

    def predict(self, input_data: str) -> str:
        return f"[{self.name} v{self.version}] 기본 추론: {input_data}"


class VisionClassifier(BaseAIModel): # 클래스 자식(부모)
    def __init__(self, name: str, version: str, resolution: str):
        super().__init__(name, version)  # 부모 초기화 코드 재사용
        self.resolution = resolution

    def predict(self, input_data: str) -> str:  # 다형성 오버라이딩
        return (
            f"[Vision {self.name} ({self.resolution})] "
            f"이미지 '{input_data}' 분석 결과 -> '고양이 (확률 98.4%)'"
        )


class TextSummarizerLLM(BaseAIModel):
    def __init__(self, name: str, version: str, max_tokens: int):
        super().__init__(name, version)
        self.max_tokens = max_tokens

    def predict(self, input_data: str) -> str:  # 다형성 오버라이딩
        summary = input_data[:18] + "..." if len(input_data) > 18 else input_data
        return (
            f"[LLM {self.name} (max={self.max_tokens})] "
            f"텍스트 요약 결과 -> '{summary}'"
        )
# pipeline = [BaseAIModel]('base','1,0'),VisionClassifier('vision','1,0','1024'), TextSummarizerLLM('textsumarizer','1,0')
# for obj in pipeline:
#     print(obj.predict('테스트'))   # 선생님 따라 추가 작성한 코드 3줄, 이 것으로 코드 리뷰했는데 아직 이해 못했음 이후 공부 필요


# 다형성의 위력: 서로 다른 모델 클래스들을 단일 for 루프로 일괄 실행!
pipeline: list[BaseAIModel] = [
    VisionClassifier("YOLO-KDT", "8.2", "640x640"),
    TextSummarizerLLM("Codex-Mini", "2.0", 512),
]

for model in pipeline:
    print(model.predict("실습 데이터 샘플 입력입니다"))


# 실행 결과:
# [Vision YOLO-KDT (640x640)] 이미지 '실습 데이터 샘플 입력입니다' 분석 결과 -> '고양이 (확률 98.4%)'
# [LLM Codex-Mini (max=512)] 텍스트 요약 결과 -> '실습 데이터 샘플 입력입니다'












# 아래는 주석 해석 포함 코드

# 멀티모달 AI 모델 통합 추론 파이프라인
#
# 먼저 제목에 나온 용어부터 알아봅시다.
#
# 멀티모달:
#   이미지, 텍스트처럼 여러 종류의 데이터를 다루는 것을 뜻합니다.
#
# 추론:
#   학습된 모델에 데이터를 넣어 예측 결과를 얻는 과정입니다.
#
# 이 예제에서는 실제 AI 연산 대신 문자열로 결과를 만들어 반환합니다.
# 이미지 분석 결과는 미리 정해진 문장이고,
# 텍스트 요약은 문자열이 길면 앞부분을 잘라 보여 주는 방식입니다.
#
# 여기서 배울 핵심 개념은 다음 세 가지입니다.
#
#   ① 상속: 다른 클래스의 속성과 기능을 물려받기
#   ② 오버라이딩: 물려받은 메서드를 자식 클래스에서 다시 정의하기
#   ③ 다형성: 같은 메서드 호출이 객체에 따라 다르게 동작하기


# 1. 여러 AI 모델이 공통으로 사용할 부모 클래스를 만듭니다.
#
# class는 데이터와 기능을 묶은 설계도를 정의하는 문법입니다.
# BaseAIModel은 우리가 지은 클래스 이름입니다.
#
# Base는 여기서 '기본이 되는'이라는 뜻으로 사용했습니다.
# 앞으로 만들 이미지 모델과 텍스트 모델의 공통 부분을 담습니다.
class BaseAIModel:

    # 2. 객체를 처음 만들 때 실행할 초기화 메서드입니다.
    #
    # def는 함수를 정의하는 문법입니다.
    # 클래스 안에 정의된 함수는 '메서드'라고 부릅니다.
    #
    # __init__은 객체를 만들 때 자동으로 실행됩니다.
    #
    # self:
    #   지금 다루는 객체 자신을 가리킵니다.
    #
    # name: str:
    #   모델 이름을 문자열로 전달받습니다.
    #
    # version: str:
    #   모델 버전을 문자열로 전달받습니다.
    #   "8.2"처럼 따옴표로 감싸면 숫자 모양이어도 문자열입니다.
    #
    # : str은 타입 힌트입니다.
    # 문자열을 기대한다는 표시이며, 입력값을 자동으로 검사하지는 않습니다.
    def __init__(self, name: str, version: str):

        # 전달받은 모델 이름을 객체에 저장합니다.
        #
        # 오른쪽 name은 전달받은 값이고,
        # 왼쪽 self.name은 객체가 계속 가지고 있을 속성입니다.
        #
        # =는 오른쪽 값을 왼쪽에 저장하는 대입 기호입니다.
        self.name = name

        # 전달받은 버전도 객체의 속성에 저장합니다.
        self.version = version

    # 3. 기본 추론 기능을 정의합니다.
    #
    # predict는 '예측하다'라는 뜻으로 지은 메서드 이름입니다.
    #
    # input_data: str:
    #   분석할 데이터를 문자열로 전달받습니다.
    #
    # -> str:
    #   처리 결과를 문자열로 돌려준다는 타입 힌트입니다.
    def predict(self, input_data: str) -> str:

        # f"..."는 문자열 안에 실제 값을 넣는 문법입니다.
        # 중괄호 {} 안의 표현식을 계산하여 그 자리에 넣습니다.
        #
        # {self.name}    → 모델 이름
        # {self.version} → 모델 버전
        # {input_data}   → 전달받은 입력 데이터
        #
        # return은 결과를 호출한 곳에 돌려주고 메서드를 끝냅니다.
        # return 자체가 화면에 출력하는 것은 아닙니다.
        return f"[{self.name} v{self.version}] 기본 추론: {input_data}"


# 4. 이미지 분류용 자식 클래스를 만듭니다.
#
# 클래스 이름 뒤 괄호 안에 BaseAIModel을 적었습니다.
# 이것은 'BaseAIModel을 상속받겠다'는 뜻입니다.
#
# BaseAIModel     → 부모 클래스
# VisionClassifier → 자식 클래스
#
# 자식 클래스는 부모의 기능을 물려받고,
# 필요한 기능을 추가하거나 다시 정의할 수 있습니다.
class VisionClassifier(BaseAIModel):

    # 이미지 모델을 초기화하는 메서드입니다.
    #
    # name, version은 부모에서도 사용하던 정보입니다.
    # resolution은 이 이미지 모델에 추가할 해상도 정보입니다.
    #
    # 예: "640x640"
    def __init__(self, name: str, version: str, resolution: str):

        # 5. 부모 클래스의 초기화 코드를 재사용합니다.
        #
        # 이 예제에서 super().__init__(...)은
        # 부모인 BaseAIModel의 __init__을 실행합니다.
        #
        # 부모의 __init__이 다음 두 작업을 처리합니다.
        #
        #   self.name = name
        #   self.version = version
        #
        # self는 파이썬이 자동으로 연결하므로 직접 전달하지 않습니다.
        #
        # 별도의 부모 객체를 새로 만드는 것이 아니라,
        # 지금 만드는 VisionClassifier 객체에 이름과 버전을 저장합니다.
        #
        # 자식 클래스가 __init__을 따로 정의했다면,
        # 부모의 초기화 작업을 실행하려고 이렇게 명시적으로 호출합니다.
        super().__init__(name, version)

        # 부모에게 맡긴 공통 정보에 더해,
        # 이미지 모델에 필요한 해상도 정보도 저장합니다.
        #
        # 이 코드에서는 해상도를 결과 안내문에 표시합니다.
        self.resolution = resolution

    # 6. 부모의 predict를 이미지 모델에 맞게 다시 정의합니다.
    #
    # 부모에도 predict가 있었지만, 자식에서도 같은 이름으로 정의했습니다.
    # 이것을 '메서드 오버라이딩'이라고 합니다.
    #
    # VisionClassifier 객체에서 predict를 호출하면
    # 아래에 정의한 이미지용 predict가 실행됩니다.
    def predict(self, input_data: str) -> str:

        # 괄호를 사용하면 긴 표현식을 여러 줄로 나눠 적을 수 있습니다.
        return (

            # 모델 이름과 해상도를 문자열에 넣습니다.
            # 문자열 마지막의 공백은 다음 문장과 한 칸 띄우기 위한 것입니다.
            f"[Vision {self.name} ({self.resolution})] "

            # 입력 데이터를 이미지 이름이나 설명처럼 표시합니다.
            #
            # '고양이 (확률 98.4%)'는 코드에 직접 적어 둔 고정 문구입니다.
            # 실제 이미지 분석으로 계산한 결과는 아닙니다.
            #
            # 위 문자열과 이 문자열은 나란히 적혀 있으므로
            # 자동으로 이어 붙어 하나의 문자열이 됩니다.
            f"이미지 '{input_data}' 분석 결과 -> '고양이 (확률 98.4%)'"
        )


# 7. 텍스트 요약용 자식 클래스를 만듭니다.
#
# TextSummarizerLLM도 BaseAIModel을 상속받습니다.
#
# 따라서 두 자식 클래스의 관계는 다음과 같습니다.
#
# BaseAIModel
#   ├─ VisionClassifier
#   └─ TextSummarizerLLM
#
# LLM은 Large Language Model, 즉 대규모 언어 모델의 줄임말입니다.
class TextSummarizerLLM(BaseAIModel):

    # 텍스트 모델을 초기화하는 메서드입니다.
    #
    # max_tokens: int:
    #   최대 토큰 수 설정을 정수로 전달받습니다.
    #
    # 토큰은 언어 모델이 텍스트를 처리하는 단위입니다.
    # 한 글자 또는 한 단어와 항상 일치하는 것은 아닙니다.
    def __init__(self, name: str, version: str, max_tokens: int):

        # 부모의 초기화 코드를 실행해
        # 이 객체에 name과 version을 저장합니다.
        super().__init__(name, version)

        # 텍스트 모델에 필요한 추가 설정을 저장합니다.
        #
        # 이 예제에서 max_tokens는 결과 안내문에 표시됩니다.
        # 아래에서 텍스트를 자르는 길이는 별도로 적힌 18을 사용합니다.
        self.max_tokens = max_tokens

    # 8. 부모의 predict를 텍스트 모델에 맞게 다시 정의합니다.
    #
    # 이름은 이미지 모델의 메서드와 똑같이 predict이지만,
    # 내부에서 수행하는 작업은 다릅니다.
    def predict(self, input_data: str) -> str:

        # 9. 입력 문자열이 길면 앞부분만 남깁니다.
        #
        # 이 줄에는 '조건 표현식'이라는 문법을 사용했습니다.
        #
        # 기본 형태:
        #   조건이 참일 때 사용할 값 if 조건 else 거짓일 때 사용할 값
        #
        # 이 코드의 조건은 다음 부분입니다.
        #
        #   len(input_data) > 18
        #
        # len(...)은 길이를 구하는 함수입니다.
        # 문자열에 사용하면 공백을 포함한 문자 수를 구합니다.
        # >는 왼쪽 값이 오른쪽 값보다 큰지 비교합니다.
        #
        # 조건이 참이면:
        #
        #   input_data[:18] + "..."
        #
        # [:18]은 처음부터 인덱스 18 직전까지 가져오는 '슬라이싱'입니다.
        # 인덱스는 0부터 시작하므로 0~17 위치의 앞 18문자를 가져옵니다.
        # + "..."는 뒤에 점 세 개를 이어 붙입니다.
        #
        # 조건이 거짓이면:
        #
        #   input_data
        #
        # 원래 문자열을 그대로 사용합니다.
        #
        # 선택한 결과를 summary라는 변수에 저장합니다.
        summary = input_data[:18] + "..." if len(input_data) > 18 else input_data

        # 위 한 줄을 익숙한 if문으로 풀면 다음과 같습니다.
        #
        # if len(input_data) > 18:
        #     summary = input_data[:18] + "..."
        # else:
        #     summary = input_data
        #
        # 여기서는 설명용 주석이므로 위 코드는 실행되지 않습니다.

        # 10. 모델 정보와 요약 결과를 문자열로 만들어 돌려줍니다.
        return (

            # 모델 이름과 최대 토큰 수 설정을 표시합니다.
            f"[LLM {self.name} (max={self.max_tokens})] "

            # 앞에서 만든 summary를 결과 안내문에 넣습니다.
            # 두 문자열은 자동으로 이어 붙습니다.
            f"텍스트 요약 결과 -> '{summary}'"
        )


# 11. 서로 다른 모델 객체들을 하나의 리스트에 담습니다.
#
# 리스트는 여러 항목을 순서대로 담는 자료형입니다.
# 대괄호 [] 안에 항목들을 적고 쉼표로 구분합니다.
#
# pipeline: list[BaseAIModel]
#
# pipeline:
#   우리가 지은 변수 이름입니다.
#
# : list[BaseAIModel]:
#   BaseAIModel 계열의 객체들을 담는 리스트라는 타입 힌트입니다.
#
# VisionClassifier와 TextSummarizerLLM은 모두
# BaseAIModel을 상속받았으므로 이 타입에 맞게 사용할 수 있습니다.
#
# 이 타입 힌트 자체가 리스트에 들어갈 값을 자동으로 검사하지는 않습니다.
pipeline: list[BaseAIModel] = [

    # 첫 번째 객체: 이미지 분류 모델
    #
    # "YOLO-KDT" → name
    # "8.2"      → version
    # "640x640"  → resolution
    #
    # VisionClassifier의 __init__이 실행되고,
    # 그 안에서 부모의 __init__도 호출됩니다.
    VisionClassifier("YOLO-KDT", "8.2", "640x640"),

    # 두 번째 객체: 텍스트 요약 모델
    #
    # "Codex-Mini" → name
    # "2.0"        → version
    # 512          → max_tokens
    #
    # TextSummarizerLLM의 __init__이 실행되고,
    # 그 안에서 부모의 __init__도 호출됩니다.
    TextSummarizerLLM("Codex-Mini", "2.0", 512),
]


# 12. 리스트에 있는 모델을 차례대로 실행합니다.
#
# for는 반복문입니다.
#
# for model in pipeline:
#
# 위 문장은 다음처럼 읽으면 됩니다.
#
#   'pipeline에서 항목을 하나씩 꺼내 model이라는 이름으로 사용하라.'
#
# 첫 번째 반복:
#   model은 VisionClassifier 객체를 가리킵니다.
#
# 두 번째 반복:
#   model은 TextSummarizerLLM 객체를 가리킵니다.
#
# 콜론 아래에 들여쓴 코드가 각 항목에 대해 실행됩니다.
for model in pipeline:

    # 13. 같은 메서드 이름으로 각 모델의 기능을 실행합니다.
    #
    # model.predict(...)라는 호출 모양은 매번 같습니다.
    #
    # 하지만 실제로 model이 가리키는 객체에 따라 실행할 메서드가 달라집니다.
    #
    # VisionClassifier 객체라면:
    #   VisionClassifier의 predict가 실행됩니다.
    #
    # TextSummarizerLLM 객체라면:
    #   TextSummarizerLLM의 predict가 실행됩니다.
    #
    # 이것이 '다형성'입니다.
    # 같은 호출 방식으로 서로 다른 객체의 동작을 사용할 수 있습니다.
    #
    # 두 자식 클래스 모두 predict를 오버라이딩했으므로,
    # 이 반복문에서는 부모의 기본 predict가 실행되지 않습니다.
    #
    # 안쪽의 predict가 결과 문자열을 반환하면,
    # 바깥쪽의 print가 그 문자열을 화면에 출력합니다.
    #
    # 두 모델 모두 같은 원본 문자열을 입력받습니다.
    print(model.predict("실습 데이터 샘플 입력입니다"))


# 실제 화면에 출력되는 두 줄:
#
# [Vision YOLO-KDT (640x640)] 이미지 '실습 데이터 샘플 입력입니다' 분석 결과 -> '고양이 (확률 98.4%)'
# [LLM Codex-Mini (max=512)] 텍스트 요약 결과 -> '실습 데이터 샘플 입력입니다'
#
#
# 텍스트 결과에 ...이 붙지 않는 이유:
#
# 입력 문자열이 18문자 이하이므로 조건 표현식의 else 쪽이 선택됩니다.
# 따라서 입력 문자열 전체가 summary에 저장됩니다.
#
#
# 버전 정보가 출력되지 않는 이유:
#
# 부모의 __init__을 통해 각 객체에 version은 저장되어 있습니다.
# 다만 자식의 predict에서 만드는 안내문에는 version을 넣지 않았습니다.
#
#
# 마지막으로 세 개념을 코드와 연결해 봅시다.
#
# 상속:
#   class VisionClassifier(BaseAIModel):
#   → 부모 클래스의 공통 구조와 기능을 물려받습니다.
#
# 오버라이딩:
#   자식 클래스에서 def predict(...)를 다시 정의합니다.
#   → 자신의 역할에 맞는 동작을 작성합니다.
#
# 다형성:
#   model.predict(...)
#   → 같은 호출로 이미지 모델과 텍스트 모델의 서로 다른 동작을 실행합니다.













# # 예제 직접 작성 선생님이 적어주신 코드 

# from abc import ABC, abstractmethod

# class paymentGateway(ABC):
#     @abstractmethod
#     def process_payment(self,item:str, amount:int) ->str:
#         # return f'구매품목 : {item} 수량 : {amount}'
#         pass

# class CreditcardGateway(paymentGateway):
#     def process_payment(self,item:str, amount:int)->str:
#         return f'구매품목2 : {item} 수량2 : {amount}'

# class BankGateway(paymentGateway):
#     pass

# obj = BankGateway()
# print(obj.process_payment('식료품',100))

# # for obj in [CreditcardGateway(), BankGatewey()]:
# #     print(obj.process_payment('a',100))


















# 다중 결제 게이트웨이 및 자동 정산 영수증 시스템

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class PaymentReceipt:
    method: str
    buyer: str
    amount: int
    fee: int
    status: str

    @property
    def net_amount(self) -> int:
        return self.amount - self.fee


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, buyer: str, amount: int) -> PaymentReceipt:
        """모든 결제 수단 클래스가 반드시 구현해야 하는 추상 메서드"""
        pass


class CreditCardGateway(PaymentGateway):
    def process_payment(self, buyer: str, amount: int) -> PaymentReceipt:
        fee = int(amount * 0.025)
        return PaymentReceipt("신용카드", buyer, amount, fee, "APPROVED")


class KakaoPayGateway(PaymentGateway):
    def process_payment(self, buyer: str, amount: int) -> PaymentReceipt:
        fee = int(amount * 0.01)
        return PaymentReceipt("카카오페이", buyer, amount, fee, "APPROVED")


gateways: list[PaymentGateway] = [
    CreditCardGateway(),
    KakaoPayGateway(),
]

for gw in gateways:
    receipt = gw.process_payment("박파이썬", 50000)
    print(f"{receipt} | 정산 금액: {receipt.net_amount:,}원")


# 실행 결과:
# PaymentReceipt(method='신용카드', buyer='박파이썬', amount=50000, fee=1250, status='APPROVED') | 정산 금액: 48,750원
# PaymentReceipt(method='카카오페이', buyer='박파이썬', amount=50000, fee=500, status='APPROVED') | 정산 금액: 49,500원





















# 아래는 주석 해석 포함 코드




# 전체 흐름:
#
#   ① 영수증에 담을 정보의 구조를 정의합니다.
#   ② 결제 수단들이 공통으로 제공해야 하는 기능을 정합니다.
#   ③ 신용카드와 카카오페이의 결제 처리 방식을 각각 구현합니다.
#   ④ 두 결제 수단을 반복문으로 실행합니다.
#   ⑤ 영수증과 정산 금액을 출력합니다.
#
# 이 예제는 실제 결제 서비스에 접속하지 않습니다.
# 수수료를 계산하고 승인 상태가 담긴 영수증 객체를 만드는 코드입니다.
#
# 2.5%와 1%는 이 예제에서 사용하는 계산 규칙입니다.


# 1. 파이썬 표준 라이브러리에서 필요한 도구를 가져옵니다.
#
# 모듈(module):
#   관련 기능을 모아 놓은 단위입니다.
#
# from 모듈이름 import 도구이름:
#   해당 모듈에서 필요한 도구를 가져오는 문법입니다.
#
# abc 모듈에서 두 가지를 가져옵니다.
#
# ABC:
#   추상 클래스의 기반으로 사용하는 클래스입니다.
#
# abstractmethod:
#   특정 메서드를 추상 메서드로 표시하는 데코레이터입니다.
from abc import ABC, abstractmethod

# dataclasses 모듈에서 dataclass를 가져옵니다.
#
# dataclass는 데이터를 담는 클래스에 필요한 메서드들을
# 자동으로 만들어 주는 데코레이터입니다.
#
# 두 모듈 모두 파이썬 표준 라이브러리에 포함되어 있습니다.
from dataclasses import dataclass


# 2. 결제 영수증을 표현할 데이터클래스를 만듭니다.
#
# @로 시작하는 문법을 '데코레이터'라고 합니다.
# 바로 아래에 정의할 클래스나 함수에 특별한 기능을 적용합니다.
#
# @dataclass를 붙이면 필드 선언을 바탕으로
# 여러 메서드를 자동으로 만들어 줍니다.
#
# 이 코드에서 특히 사용하는 기능은 다음 두 가지입니다.
#
# __init__:
#   전달받은 값을 객체의 속성에 저장하는 초기화 메서드입니다.
#
# __repr__:
#   객체에 어떤 데이터가 들어 있는지 보여 주는 문자열 표현을 만듭니다.
@dataclass
class PaymentReceipt:

    # 다음 다섯 줄은 영수증에 필요한 필드들을 선언한 것입니다.
    #
    # 필드(field):
    #   여기서는 데이터클래스가 관리할 개별 데이터 항목을 말합니다.
    #
    # : str과 : int는 타입 힌트입니다.
    # 어떤 종류의 값을 기대하는지 알려 주지만,
    # 그 자체로 값의 종류를 자동 검사하지는 않습니다.

    # 결제 수단 이름입니다.
    # 예: "신용카드", "카카오페이"
    #
    # method는 여기서 '결제 방식'이라는 뜻으로 사용한 필드 이름입니다.
    method: str

    # 구매자 이름입니다.
    # 예: "박파이썬"
    buyer: str

    # 결제 금액입니다.
    # 예: 50000
    amount: int

    # 수수료입니다.
    # 예: 1250
    fee: int

    # 처리 상태입니다.
    # 예: "APPROVED"
    #
    # APPROVED는 '승인됨'이라는 뜻의 문자열입니다.
    status: str

    # 위의 필드 선언을 바탕으로 dataclass가 초기화 기능을 만듭니다.
    #
    # 개념적으로 다음과 같은 작업을 자동으로 준비해 줍니다.
    #
    # def __init__(self, method, buyer, amount, fee, status):
    #     self.method = method
    #     self.buyer = buyer
    #     self.amount = amount
    #     self.fee = fee
    #     self.status = status
    #
    # 따라서 우리가 __init__을 직접 작성하지 않아도
    # PaymentReceipt(...)로 값을 전달하여 객체를 만들 수 있습니다.

    # 3. 정산 금액을 읽을 수 있는 속성을 정의합니다.
    #
    # @property를 붙이면 메서드를 괄호 없이 속성처럼 읽을 수 있습니다.
    #
    # 사용 예:
    #   receipt.net_amount
    #
    # 이렇게 읽을 때 아래 메서드가 실행됩니다.
    @property
    def net_amount(self) -> int:

        # self는 지금 정산 금액을 구하는 영수증 객체 자신입니다.
        # -> int는 정수 값을 반환한다는 타입 힌트입니다.
        #
        # 이 예제의 정산 금액 계산:
        #   결제 금액 - 수수료
        #
        # 예:
        #   50000 - 1250 = 48750
        #
        # net_amount를 읽을 때마다 현재 amount와 fee로 계산합니다.
        # 계산 결과를 별도 필드에 저장하는 방식은 아닙니다.
        return self.amount - self.fee


# 4. 결제 수단들이 따라야 할 공통 규칙을 정의합니다.
#
# PaymentGateway는 여기서 결제 처리를 담당하는 클래스의 공통 부모입니다.
#
# 괄호 안의 ABC는 상속받을 부모 클래스입니다.
# ABC를 기반으로 추상 클래스를 정의합니다.
#
# 추상 클래스는 공통 구조와 구현 규칙을 정하는 데 사용할 수 있습니다.
class PaymentGateway(ABC):

    # 5. 결제 처리 기능을 추상 메서드로 선언합니다.
    #
    # @abstractmethod는 아래 메서드가
    # 아직 구체적으로 구현되지 않은 추상 메서드임을 표시합니다.
    #
    # 이 추상 메서드가 구현되지 않은 상태에서는 객체를 만들 수 없습니다.
    #
    # 예:
    #   PaymentGateway()
    #   → TypeError 발생
    #
    # 자식 클래스가 실제 객체를 만들 수 있으려면
    # 이 추상 메서드에 대한 구현이 마련되어 있어야 합니다.
    @abstractmethod
    def process_payment(self, buyer: str, amount: int) -> PaymentReceipt:

        # buyer:
        #   구매자 이름을 전달받습니다.
        #
        # amount:
        #   결제 금액을 전달받습니다.
        #
        # -> PaymentReceipt:
        #   결제 결과로 PaymentReceipt 객체를 반환한다는 타입 힌트입니다.

        # 클래스나 함수 정의 바로 아래에 적은 설명 문자열을
        # '독스트링(docstring)'이라고 합니다.
        """모든 결제 수단 클래스가 반드시 구현해야 하는 추상 메서드"""

        # 여기서는 구체적인 결제 처리 코드를 작성하지 않았습니다.
        # pass는 아무 작업도 하지 않는 문법입니다.
        #
        # 이 자리는 자식 클래스가 구현할 기능의 틀을 보여 줍니다.
        pass


# 6. 신용카드 결제용 자식 클래스를 정의합니다.
#
# PaymentGateway를 상속받습니다.
# 부모가 요구한 process_payment를 아래에서 구체적으로 구현합니다.
class CreditCardGateway(PaymentGateway):

    # 부모의 메서드를 같은 이름으로 다시 정의합니다.
    # 이것을 '오버라이딩'이라고 합니다.
    def process_payment(self, buyer: str, amount: int) -> PaymentReceipt:

        # 7. 신용카드 수수료를 계산합니다.
        #
        # *는 곱하기입니다.
        # 0.025는 2.5%를 소수로 표현한 값입니다.
        #
        # 결제 금액이 50000원이면:
        #   50000 * 0.025 = 1250.0
        #
        # int(...)는 값을 정수로 변환합니다.
        # 소수 부분이 있다면 제거하며, 반올림하는 기능은 아닙니다.
        #
        # 여기서는 int(1250.0)이므로 1250이 됩니다.
        fee = int(amount * 0.025)

        # 8. 계산한 내용으로 영수증 객체를 만들어 반환합니다.
        #
        # PaymentReceipt의 필드 선언 순서대로 값을 전달합니다.
        #
        # "신용카드" → method
        # buyer      → buyer
        # amount     → amount
        # fee        → fee
        # "APPROVED" → status
        #
        # @dataclass가 자동으로 만든 __init__이
        # 이 값들을 새 영수증 객체에 저장합니다.
        #
        # return으로 돌려주는 것은 단순한 문자열이 아니라
        # 다섯 필드가 담긴 PaymentReceipt 객체입니다.
        return PaymentReceipt("신용카드", buyer, amount, fee, "APPROVED")


# 9. 카카오페이 결제용 자식 클래스를 정의합니다.
#
# 이 클래스도 PaymentGateway를 상속받습니다.
#
# 두 결제 클래스는 같은 부모를 가지지만,
# 수수료 계산 규칙은 각각 다르게 구현합니다.
class KakaoPayGateway(PaymentGateway):

    # 메서드 이름과 사용하는 방식은 신용카드 쪽과 같습니다.
    # 내부 계산이 카카오페이 규칙에 맞게 달라집니다.
    def process_payment(self, buyer: str, amount: int) -> PaymentReceipt:

        # 카카오페이 수수료를 계산합니다.
        #
        # 0.01은 1%를 소수로 표현한 값입니다.
        #
        # 결제 금액이 50000원이면:
        #   50000 * 0.01 = 500.0
        #   int(500.0) = 500
        fee = int(amount * 0.01)

        # 결제 수단 이름을 "카카오페이"로 넣고
        # 계산한 수수료와 함께 새 영수증 객체를 만들어 반환합니다.
        #
        # "APPROVED"는 코드에서 직접 넣는 상태 문자열입니다.
        return PaymentReceipt("카카오페이", buyer, amount, fee, "APPROVED")


# 10. 사용할 결제 처리 객체들을 하나의 리스트에 담습니다.
#
# gateways:
#   우리가 지은 변수 이름입니다.
#
# : list[PaymentGateway]:
#   PaymentGateway 계열의 객체들을 담는 리스트라는 타입 힌트입니다.
#
# CreditCardGateway와 KakaoPayGateway는 모두
# PaymentGateway를 상속받으므로 이 타입에 맞게 사용할 수 있습니다.
#
# 타입 힌트 자체가 리스트에 들어오는 항목을 자동으로 검사하지는 않습니다.
gateways: list[PaymentGateway] = [

    # 신용카드 결제 처리 객체를 만듭니다.
    # 아직 process_payment를 호출한 것은 아닙니다.
    CreditCardGateway(),

    # 카카오페이 결제 처리 객체를 만듭니다.
    KakaoPayGateway(),
]


# 11. 결제 수단을 하나씩 꺼내 실행합니다.
#
# for는 반복문입니다.
#
# for gw in gateways:
#   gateways에서 항목을 하나씩 꺼내 gw라는 이름으로 사용합니다.
#
# gw는 gateway를 줄여서 지은 변수 이름입니다.
# 파이썬이 정해 둔 특별한 단어는 아닙니다.
#
# 첫 번째 반복:
#   gw는 CreditCardGateway 객체를 가리킵니다.
#
# 두 번째 반복:
#   gw는 KakaoPayGateway 객체를 가리킵니다.
for gw in gateways:

    # 12. 현재 결제 수단으로 결제를 처리합니다.
    #
    # "박파이썬" → buyer
    # 50000      → amount
    #
    # 호출하는 코드의 모양은 매번 같습니다.
    #
    # 하지만 gw가 실제로 가리키는 객체에 따라 실행되는 메서드가 달라집니다.
    #
    # 신용카드 객체:
    #   CreditCardGateway.process_payment 실행
    #   → 수수료 1250원인 영수증 반환
    #
    # 카카오페이 객체:
    #   KakaoPayGateway.process_payment 실행
    #   → 수수료 500원인 영수증 반환
    #
    # 이렇게 같은 호출 방식으로 서로 다른 동작을 사용하는 것이
    # '다형성'입니다.
    #
    # 반환된 영수증 객체를 receipt라는 변수에 저장합니다.
    receipt = gw.process_payment("박파이썬", 50000)

    # 13. 영수증 정보와 정산 금액을 출력합니다.
    #
    # f"..."는 문자열 안에 값을 넣는 문법입니다.
    #
    # {receipt}:
    #   영수증 객체를 문자열로 표현합니다.
    #
    # dataclass가 자동 생성한 __repr__ 덕분에
    # 다음처럼 필드 이름과 값이 함께 표시됩니다.
    #
    #   PaymentReceipt(method='신용카드', buyer='박파이썬', ...)
    #
    # {receipt.net_amount:,}:
    #   먼저 @property가 붙은 net_amount를 실행해 정산 금액을 구합니다.
    #   이어서 :, 형식으로 천 단위 쉼표를 붙여 표시합니다.
    #
    # 예:
    #   48750 → "48,750"
    #
    # 쉼표는 출력 형식이며, 실제 숫자 값 자체를 바꾸지는 않습니다.
    #
    # |와 '정산 금액:', '원'은 화면에 그대로 표시할 문자입니다.
    print(f"{receipt} | 정산 금액: {receipt.net_amount:,}원")


# 실제 화면에 출력되는 두 줄:
#
# PaymentReceipt(method='신용카드', buyer='박파이썬', amount=50000, fee=1250, status='APPROVED') | 정산 금액: 48,750원
# PaymentReceipt(method='카카오페이', buyer='박파이썬', amount=50000, fee=500, status='APPROVED') | 정산 금액: 49,500원
#
#
# 계산 과정을 다시 확인해 봅시다.
#
# 신용카드:
#   결제 금액 50000원
#   수수료 50000 × 0.025 = 1250원
#   정산 금액 50000 - 1250 = 48750원
#
# 카카오페이:
#   결제 금액 50000원
#   수수료 50000 × 0.01 = 500원
#   정산 금액 50000 - 500 = 49500원
#
#
# 각 문법의 역할을 연결해 봅시다.
#
# @dataclass
#   → 영수증 데이터를 저장하고 표현하는 기본 기능을 자동으로 만듭니다.
#
# ABC와 @abstractmethod
#   → 결제 처리 클래스가 구현해야 할 공통 기능을 정합니다.
#
# 상속
#   → 두 결제 클래스가 PaymentGateway의 구조를 물려받습니다.
#
# 오버라이딩
#   → 각 결제 클래스가 process_payment를 자기 방식으로 구현합니다.
#
# 다형성
#   → 같은 gw.process_payment(...) 호출이 객체에 따라 다르게 동작합니다.
#
# @property
#   → receipt.net_amount처럼 읽을 때 정산 금액을 계산합니다.