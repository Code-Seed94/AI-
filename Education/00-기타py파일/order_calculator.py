from decimal import Decimal, localcontext
from typing import Union


# 수정: 등급별 결제 비율과 쿠폰 금액을 이름 있는 상수로 분리합니다.
PAYMENT_RATES = {
    1: Decimal("0.95"),  # 5% 할인
    2: Decimal("0.90"),  # 10% 할인
    3: Decimal("0.80"),  # 20% 할인
}
COUPON_DISCOUNT = Decimal("3000")


def calc_order_legacy(
    u_type: int,
    price: Union[int, float, Decimal],
    qty: int,
    coupon: str,
) -> int:
    """등급 할인 후 쿠폰을 차감하고, 0 이상으로 보정한 뒤 소수부를 버립니다.

    단가는 0 이상의 유한한 수, 수량은 양의 정수여야 합니다.
    쿠폰은 공백과 대소문자를 정리한 YES 또는 NO만 허용합니다.
    기존 호출부와의 호환을 위해 함수 이름과 매개변수 이름을 유지합니다.
    """
    # 수정: True가 1로 취급되지 않도록 정확히 int 타입인지 확인합니다.
    if type(u_type) is not int:
        raise TypeError("u_type은 정수여야 합니다.")
    if u_type not in PAYMENT_RATES:
        raise ValueError("u_type은 1, 2, 3 중 하나여야 합니다.")

    # 수정: 음수, 0, 소수, 불리언 수량을 계산 전에 거부합니다.
    if type(qty) is not int:
        raise TypeError("qty는 정수여야 합니다.")
    if qty <= 0:
        raise ValueError("qty는 1 이상이어야 합니다.")

    # 수정: 숫자가 아닌 단가와 숫자처럼 동작하는 bool을 거부합니다.
    if isinstance(price, bool) or not isinstance(price, (int, float, Decimal)):
        raise TypeError("price는 int, float 또는 Decimal이어야 합니다.")

    # 수정: Decimal(float) 대신 문자열로 변환하여 이진 소수 오차를 피합니다.
    unit_price = Decimal(str(price))
    if not unit_price.is_finite() or unit_price < 0:
        raise ValueError("price는 0 이상의 유한한 수여야 합니다.")

    # 수정: 쿠폰 표기를 정리하고, 잘못된 값은 미사용으로 처리하지 않습니다.
    if not isinstance(coupon, str):
        raise TypeError("coupon은 문자열이어야 합니다.")
    normalized_coupon = coupon.strip().upper()
    if normalized_coupon not in ("YES", "NO"):
        raise ValueError("coupon은 YES 또는 NO여야 합니다.")

    # 수정: 큰 금액이나 긴 소수도 기본 정밀도 때문에 반올림되지 않게 합니다.
    price_parts = unit_price.as_tuple()
    required_precision = (
        len(price_parts.digits)
        + max(price_parts.exponent, 0)
        + len(str(qty))
        + 4
    )
    with localcontext() as context:
        # 이 함수의 정밀도 변경은 다른 코드의 Decimal 설정에 영향을 주지 않습니다.
        context.prec = max(28, required_precision)
        total = unit_price * qty * PAYMENT_RATES[u_type]
        if normalized_coupon == "YES":
            total -= COUPON_DISCOUNT

        # 기존 정책 유지: 쿠폰 차감 후 최솟값은 0, 최종 소수부는 버립니다.
        return max(0, int(total))
