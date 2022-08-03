import random


class DevilsBones:
    def __init__(self):
        self.digits = [i for i in range(1,7)]

    def __repr__(self):
        return 'Экземпляр класса DevilsBones'

    def throw_bones(self):
        """Возвращает значение двух подброшенных костей"""
        result = tuple(random.sample(self.digits, 2))
        return result





