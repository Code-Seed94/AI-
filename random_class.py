"""랜덤 클래스 코드를 생성하는 유틸리티."""

import secrets
import string


class RandomClassCodeGenerator:
    """대문자와 숫자를 조합해 중복 가능성이 낮은 코드를 생성한다."""

    def __init__(self, length: int = 8) -> None:
        if length < 1:
            raise ValueError("코드 길이는 1 이상이어야 합니다.")
        self.length = length
        self._alphabet = string.ascii_uppercase + string.digits

    def generate(self) -> str:
        """랜덤 코드 하나를 반환한다."""
        return "".join(secrets.choice(self._alphabet) for _ in range(self.length))

    def generate_many(self, count: int) -> list[str]:
        """지정한 개수만큼 랜덤 코드를 반환한다."""
        if count < 0:
            raise ValueError("생성 개수는 0 이상이어야 합니다.")
        return [self.generate() for _ in range(count)]


if __name__ == "__main__":
    generator = RandomClassCodeGenerator()
    print(generator.generate())
