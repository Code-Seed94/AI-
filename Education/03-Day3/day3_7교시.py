#  온라인 서점 주문/할인 계산기 Before & After 완벽 비교


# Before: 리팩토링 전
# 매직 넘버와 if-elif가 얽힌 취약한 절차지향 함수

def calc_order_legacy(u_type, price, qty, coupon):
    # 문제점 1: u_type 1, 2, 3이 무슨 등급인지 작성자 외에는 알 수 없음
    # 문제점 2: price나 qty에 음수가 들어와도 아무런 검증 없이 금액을 계산함
    total = price * qty

    if u_type == 1:
        total = total * 0.95
    elif u_type == 2:
        total = total * 0.90
    elif u_type == 3:
        total = total * 0.80

    if coupon == "YES":
        total = total - 3000

    if total < 0:
        total = 0

    return int(total)


# After: 리팩토링 후
# 불변 데이터클래스 + 상수 테이블 + 커스텀 예외 검증

from dataclasses import dataclass


class InvalidOrderError(ValueError):
    """주문 데이터 또는 멤버십 등급이 유효하지 않을 때 발생하는 도메인 예외"""
    pass


@dataclass(frozen=True)
class OrderItem:
    name: str
    unit_price: int
    quantity: int

    def __post_init__(self):
        if self.unit_price < 0 or self.quantity <= 0:
            raise InvalidOrderError(
                f"유효하지 않은 가격({self.unit_price}) "
                f"또는 수량({self.quantity})입니다."
            )

    @property
    def subtotal(self) -> int:
        return self.unit_price * self.quantity


class MembershipCheckout:
    DISCOUNT_RATES = {
        "BASIC": 0.05,
        "GOLD": 0.10,
        "VIP": 0.20,
    }

    COUPON_AMOUNT = 3000

    def calculate_final_price(
        self,
        item: OrderItem,
        tier: str,
        use_coupon: bool = False,
    ) -> int:
        if tier not in self.DISCOUNT_RATES:
            raise InvalidOrderError(
                f"알 수 없는 멤버십 등급입니다: '{tier}'"
            )

        discount_rate = self.DISCOUNT_RATES[tier]
        discounted = int(item.subtotal * (1.0 - discount_rate))

        if use_coupon:
            discounted -= self.COUPON_AMOUNT

        return max(0, discounted)


checkout = MembershipCheckout()
book_order = OrderItem("파이썬 클린 아키텍처", 15000, 2)

print("Before 결과:", calc_order_legacy(2, 15000, 2, "YES"))

print(
    "After 결과:",
    checkout.calculate_final_price(
        book_order,
        tier="GOLD",
        use_coupon=True,
    ),
)


# 실행 결과:
# Before 결과: 24000
# After 결과: 24000