# class BaristaBot:
#     def __init__(self, bot_name: str, bean_grams: int): # __init__ 은 생성자라고 한다
#         self.bot_name = bot_name # 객체 자신의 속성을 정하는데 똑같이 이름을 맞춰서 통일성, 가독성을 준다
#         self.bean_grams = bean_grams # 위와 같이 이해한다
#         self.total_cups = 0 # 만든 잔 수를 말하는데 처음이니까 0으로 맞춘다 

#     def brew_espresso(self, cups: int = 1) -> str:
#         required_beans = cups * 13
#         if self.bean_grams < required_beans:
#             return f"[{self.bot_name}] 원두 부족! (필요: {required_beans}g, 현재:{self.bean_grams}g)"
        
#         self.bean_grams -= required_beans
#         self.total_cups += cups
#         return f"[{self.bot_name}] 에스프레소 {cups}잔 추출 완료! (남은 원두:{self.bean_grams}g, 누적: {self.total_cups}잔)"
# bot = BaristaBot("코덱스바리스타-1호", 50)
# print(bot.brew_espresso(4))
# # print(bot.brew_espresso())

# # 실행 결과:
# # [코덱스바리스타-1호] 에스프레소 2잔 추출 완료! (남은 원두: 14g, 누적: 2잔)
# # [코덱스바리스타-1호] 원두 부족! (필요: 36g, 현재: 14g)








# 수정된 코드



class BaristaBot:
    def __init__(self, bot_name: str, bean_grams: int):
        self.bot_name = bot_name
        self.bean_grams = bean_grams
        self.total_cups = 0

    def brew_espresso(self, cups: int = 1) -> str:
        possible_cups = self.bean_grams // 13
        made_cups = min(possible_cups, cups)
       

        self.bean_grams -= made_cups * 13
        self.total_cups += made_cups

        unmade_cups = cups - made_cups

        if unmade_cups > 0:
            return (
                f"{made_cups}잔 추출 완료! "
                f"남은 원두: {self.bean_grams}g. "
                f"원두가 부족해서 나머지 {unmade_cups}잔은 만들 수 없습니다."
            )

        return (
            f"{made_cups}잔 추출 완료! "
            f"남은 원두: {self.bean_grams}g."
        )


bot = BaristaBot("코덱스바리스타-1호", 50)
print(bot.brew_espresso(4))


