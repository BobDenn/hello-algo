import random


class Game:
    top_score = 0

    def __init__(self, name):
        self.name = name  # 实例属性

    # 类方法
    @classmethod
    def show_top_score(cls):
        print(f"游戏的最高分是{cls.top_score}")

    def start_game(self):
        score = random.randint(1, 100)
        print(f"玩家{self.name}得分{score}")
        if score > Game.top_score:
            Game.top_score = score

    @staticmethod
    def show_help():
        print("------这是游戏帮助信息------")


if __name__ == '__main__':
    Game.show_help()
    Game.show_top_score()
    player1 = Game('xiaodeng')
    player1.start_game()
    player1.show_top_score()
