# AI Git Starter

Python 학습 저장소입니다.

## 랜덤 클래스 코드 생성기

`random_class.py`의 `RandomClassCodeGenerator` 클래스는 대문자와 숫자를 조합한 랜덤 코드를 생성합니다.

```python
from random_class import RandomClassCodeGenerator

generator = RandomClassCodeGenerator(length=8)
print(generator.generate())
```

기본 코드 길이는 8자리이며, `generate_many(count)`로 여러 개의 코드를 한 번에 생성할 수 있습니다.
